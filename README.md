# **TIRALABRA**

Ohjelma koodataan käyttäen Python-kieltä.

## **Huomioita Python-versioista**

Ohjelma on testattu ja toiminta varmistettu Python 3.9.7 -versiolla. Aiempien versioiden kanssa toimintaa ei voida taata.

## **Dokumentaatio**

**[Määrittelydokumentti](https://github.com/vtonteri/Algoritmisovellus/blob/master/dokumentaatio/maarittelydokumentti.md)**

**[Toteutusdokumentti](https://github.com/vtonteri/Algoritmisovellus/blob/master/dokumentaatio/toteutusdokumentti.md)**

**Testausdokumentti**

**Tuntikirjanpito**

# **Viikkoraportit**

**[Viikkoraportti 1](https://github.com/vtonteri/Algoritmisovellus/blob/master/dokumentaatio/viikkoraportti1.md)**

**[Viikkoraportti 2](https://github.com/vtonteri/Algoritmisovellus/blob/master/dokumentaatio/viikkoraportti2.md)**

**[Viikkoraportti 3](https://github.com/vtonteri/Algoritmisovellus/blob/master/dokumentaatio/viikkoraportti3.md)**

**[Viikkoraportti 4](https://github.com/vtonteri/Algoritmisovellus/blob/master/dokumentaatio/viikkoraportti4.md)**

# **Ohjelma käyttöohje**

## **Asennus ja käyttö**

1. Lataa Githubin Release

2. Asenna riippuvuudet komennolla:

`poetry install`

3. Käynnistä algoritmi ajamalla *sovellus/src* -kansiossa seuraava komento:

`poetry shell`

jonka jälkeen

`python main.py`

## **Releases**

**[Ensimmäisen vertaisarvioinnin release](https://github.com/vtonteri/Algoritmisovellus/releases/tag/v.0.4)**

Huomioita tämän hetken versiosta:

1. Ohjelman main.py metodissa on toteutettu vain kahden tilan perusteella painokertoimet määrittävä toiminnallisuus. Tilojen määrä on kovakoodattu. En ehtinyt toteuttamaan loppuun asti opi_opetusdatasta.py luokkaan täysin toimivaa, eri tiloja huomioivaa toiminnallisuutta

2. Main.py metodin ajaminen tuottaa tuloksena tulosteen, jossa on syötteenä annettujen nuottien (18 tarkoittaa nuottia g) seuraavat nuotit ja niiden painokertoimet, eli niiden esiintymistodennäköisyys (painokerroin lasketaan kumulatiivisesti; tämän hetkinen tuloste on 17: 0.4, 18: 1.0, mikä tarkoittaa, että todennäköisyys valita seuraavaksi 17 (eli f) on 0.4 ja todennäköisyys valita seuraavaksi 18 (eli g) on 1-0.4 = 0.6). Muunnin numeroiden ja nuottien välillä on luo_opetusdata.py luokassa.

3. Painokertoimien esiintyvyyttä voi vaihdella ja tutkia muuttamalla main.py:ssä syötteenä annettavaa nuotit -listan sisältöä. algoritmi toimii tällä hetkellä vain listoilla, jotka sisältävät yksi tai kaksi nuottia. 

4. Ainoastaan sävellaji "G" on toiminnassa ohjelman tämänhetkisessä versiossa.