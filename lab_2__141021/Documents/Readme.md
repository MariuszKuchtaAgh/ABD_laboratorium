## Mariusz Kuchta gr. 2a (czw. 10.00 - 11.30)

### Laboratoria 2 - 14.10.21
#### TIER protocol i tidy data

Zawartość folderów:

- OriginalData

-- tb.csv

Dane o gruźlicy w różnych grupach pacjentów

- AnalysisData

-- tb_melted.csv

Dane o zmniejszonej liczbie kolumn. Kolumny odpowiadające różnym typom zakażeń zostały zastąpione dwoma oznaczającymi typ zakażeń oraz ilość zakażeń danego typu.

-- tb_tidy.csv

Rozdzielenie kolumny z typami na dwie kolumny zawierające informacje o płci i wieku zakażonych. Z racji charakterystyki danych dodane zostało trzecie oznaczenie płci oraz dodatkowe oznaczenie wieku, które wskazuje na sumę zakażeń, ponieważ w wielu przypadkach oryginalny plik zawierał jedynie najbardziej ogólen informacje

-- tb_nona.csv

Plik tb_tidy z usuniętymi wierszami o wartościach NaN w kolumnie 'cases'

- CommandFiles

-- lab_2__141021_Mariusz_Kuchta.ipynb

Notebook jupyter'a przetwarzający dane z OriginalData/tb.csv

