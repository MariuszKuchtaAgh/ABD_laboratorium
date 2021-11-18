## Meta data

#### Mariusz Kuchta gr. 2a (czw. 10.00 - 11.30)
#### Laboratorium 6 - 18.11.21

* Plik 13_WARMINSKO-MAZURSKIE.csv

	* kolumna 0:
	  
			liczba całkowita
			indeks danego rekordu, zaczyna się od 0

	* kolumna 1: 'Dni od zakupu'
	  
			liczba całkowita
			liczba dni od zakupu, po których została wystawiona ocena, minimalna dopuszczalna wartość to 1
		
	* kolumna 2: 'Marka'
	  
			łańcuch znaków
			nazwa marki odkurzacza, dla którego wystawiona jest ocena, używane wartości: 'Dyson', 'Beko', 'Electrolux', 'Samsung', 'Tefal'
	  
	* kolumna 3: 'Wiek kupującego'
	  
			liczba zmiennoprzecinkowa
			wiek kupującego, który wystawił ocenę, używane wartości nie korzystają z części ułamkowej, zabronione wartości ujemne, możliwe wartości NaN

	* kolumna 4: 'Płeć kupującego'
	  
			łańcuch znaków
			płeć kupującego, który wystawił ocenę, używane wartości to 'K' - oznacza kobietę, 'M' - oznacza mężczyznę, 'bd.' - brak danych

	* kolumna 5: 'Ocena'
	  
			liczba zmiennoprzecinkowa
			wystawiona ocena przez kupującego, używane wartości od 0.0 do 5.0 (2.0, 1.0, 2.5, 4.0, 3.5, 4.5, 1.5, 0.0, 3.0, 0.5, 5.0), brak wartości NaN