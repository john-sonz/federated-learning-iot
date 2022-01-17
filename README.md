# federated-learning-iot

## Uruchomienie klientów i serwera poza Dockerem:

1. Zainstalować 'poetry' : https://python-poetry.org/docs/
1. Zainstalować potrzebne pakiety dla serwera: w folderze 'federated-learning-iot\server' uruchomić komendę `poetry install`
1. Zainstalować potrzebne pakiety dla klienta: w folderze 'federated-learning-iot\client' uruchomić komendę `poetry install`
1. Uruchomić serwer : w folderze 'federated-learning-iot\server' uruchomić komendę `poetry run python server/main.py`
1. Uruchomić klientów :
   Dla każdego klienta w Windowsie trzeba ustawić sobie tymczasową zmienną środowiskową (numerek dla klienta, najlepiej dawać po kolei 1,2,3,...):
   `set CLIENT_ID=1`
   Później odpalamy klienta analogicznie jak serwer : w folderze 'federated-learning-iot\client' uruchomić komendę
   `poetry run python client/main.py`

   W Linuksie trzeba zrobić to samo, tylko że jest nieco prościej. Wszystko załatwiamy jedną komendą.

W folderze `federated-learning-iot\client` uruchomić komendę `CLIENT_ID=1 poetry run python client/main.py`

Domyślne ustawienia są takie, że trzeba uruchomić 5 klientów żeby FML się uruchomił.

## Uruchomienie klientów i serwera jako kontenerów Dockera:

Uruchomienie trybu `swarm`.

```
docker swarm init
```

Utworzenie lokalnego dockerowego `registry` do przechowywania obrazów klienta i serwera.

```
docker service create --name registry --publish published=5000,target=5000 registry:2
```

Zbudowanie obrazów.

```
docker-compose build
```

Wysłanie zbudowanych obrazów do lokalnego `registry`.

```
docker-compose push
```

Deploy dockerowego stosu kontenerów.

```
docker stack deploy --compose-file docker-compose.yml federated-learning
```

Ilość uruchomionych klientów można kontrolować za pomocą komendy:

```
docker service scale federated-learning_client=<N>
```
