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
- Post game näkymä josta pääsee seuraavaan tasoon tai päävalikkoon
- Lisätty "level select" näkymä
- Vaihdettu autojen ulkonäköä
- Lisätty pylint ja autopep8
- Purettu funktioita pienempiin osiin pylintin ohjeiden mukaan
- Korjattu autojen testaukset ja lisätty päävalikon testit
- Lisätty play_level attribuutti
	- Mahdollistaa muun kuin seuraavan tason pelaamisen
- Lisätty tasoja
- Erotettu logiikka UI elementeistä kaikista näkymistä
- Muutettu kansiorakennetta

### Viikko 5

- Lisätty toimiva high scores näkymä
- Lisätty testikattavuutta
- Lisätty vahvistus-boksi käyttäjän poistamiseen
- Lisätty maksimipituus käyttäjänimelle (10 merkkiä)

### Viikko 6 

- Lisätty docstring dokumentointi kaikkiin tiedostoihin
- Lisätty tason korostus tasovalikkoihin kun hiiri on tason päällä
- Lisätty resoluutiovalikko
	- Peli skaalaa UI elementit ja inputit valitun resoluution mukaan
- Lisätty tasoja
