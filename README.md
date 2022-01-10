# federated-learning-iot

Uruchomienie:
1. Zainstalować 'poetry' : https://python-poetry.org/docs/  
1. zainstalować potrzebne pakiety dla serwera: w folderze 'federated-learning-iot\server' uruchomić komendę `poetry install`
2. zainstalować potrzebne pakiety dla klienta: w folderze 'federated-learning-iot\client' uruchomić komendę `poetry install`
3. uruchomić serwer : w folderze 'federated-learning-iot\server' uruchomić komendę `poetry run python server/main.py`
4. uruchomić klientów :
Dla każdego klienta w Windowsie trzeba ustawić sobie tymczasową zmienną środowiskową (numerek dla klienta, najlepiej dawać po kolei 1,2,3,...):
`set CLIENT_ID=1`  
Później odpalamy klienta analogicznie jak serwer : w folderze 'federated-learning-iot\client' uruchomić komendę  
`poetry run python client/main.py`

W Linuxie trzeba zrobić to samo, tylko że jest nieco prościej. Wszystko załatwiamy jedną komendą.
W folderze w folderze 'federated-learning-iot\client' uruchomić komendę `CLIENT_ID=1 poetry run python client/main.py`

Domyślne ustawienia są takie, że trzeba uruchomić 5 klientów żeby FML się uruchomił.
