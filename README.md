Zadanie 1 i 2 są rozwiązane w pliku save_data.py. 

Zadanie 3 - w pliku flask_app.py.

Zadanie 4 - w folderze invicta-zadanie/app/tests.

# Uruchamianie i testowanie aplikacji

Aplikację można pobrać np. wpisując w terminalu komendę:

`git clone https://github.com/emge1/invicta-zadanie.git`

Po pobraniu aplikacji, zaleca się otwarcie pobranego folderu w PyCharmie, tam utworzenie środowiska wirtualnego i uruchomienie 
go, po czym, w terminalu (będąc w folderze /invicta-zadanie) wpisać komendę:

`pip install -r requirements.txt`

w celu zainstalowania użytych bibliotek (Flask, requests i pytest).

Następnie trzeba jednokrotnie uruchomić program save_data.py - program pobiera dane i tworzy bazę danych database.db.

Potem należy upewnić się, że port 8080 na localhoście jest wolny, po czym uruchomić program flask_app.py. Wtedy, pod 
adresem http://localhost:8080/ będzie strona, z której istnieje możliwość przekierowania do pobrania dynamicznie 
generowanego pliku .csv.

Programy z testami (każdy odpowiada jednemu programowi z folderu invicta-zadanie/app) wystarczy po prostu uruchomić.


