import flwr as fl
import os

from flwr.server.strategy import FedAvg

os.environ["TF_CPP_MIN_LOG_LEVEL"] = "3"

ENV = os.environ

FRACTION_FIT = float(ENV.get('FRACTION_FIT', "0.5"))
NUM_OF_CLIENTS = int(ENV.get('NUM_OF_CLIENTS', "5"))
NUM_ROUNDS = int(ENV.get('NUM_ROUNDS', "10"))
SERVER_ADDRESS = ENV.get('SERVER_ADDRESS', "localhost:8080")

def start_server(num_rounds: int, num_clients: int, fraction_fit: float):
    strategy = FedAvg(min_available_clients=num_clients, fraction_fit=fraction_fit)
    fl.server.start_server(SERVER_ADDRESS, strategy=strategy, config={"num_rounds": num_rounds})


if __name__ == "__main__":
    start_server(NUM_ROUNDS, NUM_OF_CLIENTS, FRACTION_FIT)
