# Zadanie 1 - "Moby Dick"

Korzystając z wybranego języka programowania dokonaj analizy treści utworu "Moby Dick".
Plik do zadania Moby Dick pobierz z: www.gutenberg.org

## Opis Zadania
- Usuń puste linie, tytuł, nazwy rozdziałów. Zapisz wynik.
- Policz ile słów znajduje się w tekście.
- Policz ile unikalnych słów znajduje się w tekście.
- Znajdź 10 najczęściej występujących słów. Podaj liczbę wystąpień tych słów.
- Sprawdź jak często występowało słowo "whale".

# Zadanie 2 - "Urlopowicz" 

## Opis zadania
### Korzystając z języka Java i Framework-a Spring napisz usługę REST, która pozwala na:
- pobranie danych o pracowniku wraz ze stanem urlopu i statusem
	- employeeStatus: PERFORMER, SLACKER
- pobranie stanu urlopu wybranego pracownika po jego ID
- zgłoszenie urlopu przez pracownika

### Użyj dostępnych narzędzi do dokumentacji API
### Podczas implementacji zastosuj znane techniki celem: 
- zepewnienia wysokiej utrzymywalności kodu
- testowalność usługi

### Założenia:
- zespół nie zdecydował jeszcze jaki typ bazy danych wybrać
- zastosuj wzorzec repository: zacznij od tzw. inMemoryRepository

### Zależności:
- usługa notyfikacji, która pozwala na wysłanie maila do przełożonego o zaistniałym zgłoszeniu - wystarczy "zaślepka"
- blok dezycyjny oparty na atrybucie pracownika: employeeStatus realizujące poniższe przypadki użycia 

# UC1: pracownik zgłasza wiecej dni urlopu niż ma dostępnych w puli
## kiedy jego status to PERFORMER 
	## wówczas pozwalamy zgłosić wniosek ponad stan (zgłoszone > dostępne)
	## informujemy przełożonego mailem
## w przeciwnym razie nie pozwalamy na zgłoszenie

# UC2: pracownik zgłasza mniej dni urlopu niż ma dostępnych w puli
## wówczas pozwalamy zgłosić taki wniosek
## informujemy przełożonego mailem

# UC2: pracownik zgłasza mniej dni urlopu niż ma dostępnych w puli
## jeśli jego status to SLACKER
## wówczas nie pozwalamy na zgłoszenie wniosku

# Proszę o przygotowanie prezentacji na rozmowę: 
- przykład użycia REST
- dokumentacja REST API
- wspólne omówienie kodu
