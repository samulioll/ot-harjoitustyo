### Viikko 1

- Luotu Car-luokka autoille, board-luokka pelilaudan tilan tallentamiseen ja muuttamiseen, ja Screen-luokka pelin piirtämiseen näytölle
- Peliruudukko ja autot piirtyvät näytölle
- Autojen sijainnit tallessa matriisissa
- Autoja voi siirtää klikkaamalla ja vetämällä
	- Autojen liikkuminen noudattaa sääntöjä

### Viikko 2

- Alkeellinen rakenne eri valikoille
	- UI_element-luokka
	- Alkeellinen graafinen ulkoasu 
- Muutettu ohjelman rakennetta
	- Jäsennelty ohjeman osat täysin uudella tavalla
	- Luotu omat moduulit pelin eri näkymille, poistettu Screen-luokka

### Viikko 3

- Lisätty invoke komennot
- Luotu pytest toiminnallisuus
- 100% testikattavuus autojen logiikalle

### Viikko 4

- Lisätty profile_maanger.py, joka hallinnoi profiileja
	Luokat yksittäiselle profiilille ja kaikille
- Lisätty "select profile" näkymä
	- Profiilinimieä klikkaamalla voi valita profiilin
- Oikean tason lataaminen profiilin peliedistyksen mukaisesti
	- Peli tallentaa tasojen läpäisyn ja antaa seuraavan tason.
- Profiilin luominen ja poistaminen toimii
	- Tekstinsyöttökenttä-luokka profile_managerin alle
- Car-, Ui_Element- ja Menus-luokat siirretty omaan objects-kansioon selkeyttämään rakennetta
