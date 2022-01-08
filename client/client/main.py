import flwr
import os
import numpy as np
import tensorflow as tf


# https://stackoverflow.com/questions/56203272/docker-compose-scaling-with-unique-environment-variable
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

ENV = os.environ

BATCH_SIZE = int(ENV.get('BATCH_SIZE', "32"))
CLIENT_ID = int(ENV.get('CLIENT_ID', "1"))
EPOCHS = int(ENV.get('EPOCHS', "5"))
NUM_OF_CLIENTS = int(ENV.get('NUM_OF_CLIENTS', "5"))
SERVER_ADDRESS = ENV.get('SERVER_ADDRESS', "localhost:8080")
STEPS_PER_EPOCH = int(ENV.get('STEPS_PER_EPOCH', "10"))

def get_dataset_portion():
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.cifar10.load_data()
    train_partitions =  list(zip(np.split(x_train, NUM_OF_CLIENTS), np.split(y_train, NUM_OF_CLIENTS)))
    test_partitions =  list(zip(np.split(x_test, NUM_OF_CLIENTS), np.split(y_test, NUM_OF_CLIENTS)))

    train_portion = train_partitions[CLIENT_ID % NUM_OF_CLIENTS]
    test_portion = test_partitions[CLIENT_ID % NUM_OF_CLIENTS]

    print(f"train portion has {len(train_portion[0])} elements")
    print(f"test portion has {len(test_portion[0])} elements")

    return train_portion, test_portion

class CifarClient(flwr.client.NumPyClient):
    def __init__(self, model, dataset):
        super().__init__()

        self.model = model
        self.dataset = dataset

    def get_parameters(self):
        return self.model.get_weights()

    def fit(self, parameters, config):
        (x_train, y_train), _ = self.dataset
        self.model.set_weights(parameters)
        self.model.fit(x_train, y_train, epochs=EPOCHS, batch_size=BATCH_SIZE, steps_per_epoch=STEPS_PER_EPOCH)
        return self.model.get_weights(), len(x_train), {}

    def evaluate(self, parameters, config):
        _, (x_test, y_test) = self.dataset

        self.model.set_weights(parameters)
        loss, accuracy = self.model.evaluate(x_test, y_test)
        return loss, len(x_test), {"accuracy": accuracy}


def main():
    dataset = get_dataset_portion()
    model = tf.keras.applications.MobileNetV2((32, 32, 3), classes=10, weights=None)
    model.compile("adam", "sparse_categorical_crossentropy", metrics=["accuracy"])

    client = CifarClient(model, dataset)
    flwr.client.start_numpy_client(SERVER_ADDRESS, client)

if __name__ == "__main__":
    print("Client", CLIENT_ID)
    main()

