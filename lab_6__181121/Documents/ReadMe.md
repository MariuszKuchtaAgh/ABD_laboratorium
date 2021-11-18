## Data Appendix

### Mariusz Kuchta gr. 2a (czw. 10.00 - 11.30)
### Laboratorium 6 - 18.11.21

Zawartość folderów:

- OriginalData:

    * 13_WARMIN╠üSKO-MAZURSKIE.csv

          Dane o ocenach odkurzaczy przez klientów. Zawiera dodatkowe informacje o kupującym i o zakupie.
  
    * Metadata:
      
        * 13_WARMIN╠üSKO-MAZURSKIE_Metadata.md
          
              Dodatkowe informacje o danych z pliku 13_WARMIN╠üSKO-MAZURSKIE.csv

- AnalysisData:

    * \[pusty folder\]
  
- CommandFiles:

    * lab_6__181121_Mariusz_Kuchta.ipynb

          Notebook jupyter'a przetwarzający dane z OriginalData/13_WARMIN╠üSKO-MAZURSKIE.csv. 
          Przedstawia podstawowe informacje z oryginalnego pliku, rysuje histogramy i inne wykresy.

- Documents:

    * DataAppendix.md
  

Podgląd drzewa katalogów: 

```
lab_6__181121   
│
└───AnalysisData
│   
└───CommandFiles
│   │   lab_6__181121_Mariusz_Kuchta.ipynb
│
└───Documents
│   │   DataAppendix.md
│
└───OriginalData
    │   13_WARMINSKO-MAZURSKIE.csv
    │
    └───Metadata
        │   13_WARMINSKO-MAZURSKIE_Metadata.md
```

# Uruchomienie projektu

Do uruchomienia skryptu potrzebny jest pakiet Anaconda w 4.10.1. Należy uruchomić jupyter-notebook a następnie otworzyć plik lab_6__181121_Mariusz_Kuchta.ipynb.
Po otworzeniu pliku należy wywołać wszsytkie komórki z kodem.
Używane są ścieżki względne. W skrypcie odczytywany jest plik znajdujący się w OriginalData/13_WARMINSKO-MAZURSKIE.csv.