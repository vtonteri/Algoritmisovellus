# **TIRALABRA**

Ohjelma koodataan käyttäen Python-kieltä.

## **Huomioita Python-versioista**

Ohjelma on testattu ja toiminta varmistettu Python 3.9.7 -versiolla. Aiempien versioiden kanssa toimintaa ei voida taata.

## **Dokumentaatio**

**[Määrittelydokumentti](https://github.com/vtonteri/Algoritmisovellus/blob/master/dokumentaatio/maarittelydokumentti.md)**

**[Toteutusdokumentti](https://github.com/vtonteri/Algoritmisovellus/blob/master/dokumentaatio/toteutusdokumentti.md)**

**[Testidokumentti](https://github.com/vtonteri/Algoritmisovellus/blob/master/dokumentaatio/testiraportti.md)**

# **Viikkoraportit**

**[Viikkoraportti 1](https://github.com/vtonteri/Algoritmisovellus/blob/master/dokumentaatio/viikkoraportti1.md)**

**[Viikkoraportti 2](https://github.com/vtonteri/Algoritmisovellus/blob/master/dokumentaatio/viikkoraportti2.md)**

**[Viikkoraportti 3](https://github.com/vtonteri/Algoritmisovellus/blob/master/dokumentaatio/viikkoraportti3.md)**

**[Viikkoraportti 4](https://github.com/vtonteri/Algoritmisovellus/blob/master/dokumentaatio/viikkoraportti4.md)**

**[Viikkoraportti 5](https://github.com/vtonteri/Algoritmisovellus/blob/master/dokumentaatio/viikkoraportti5.md)**

**[Viikkoraportti 6](https://github.com/vtonteri/Algoritmisovellus/blob/master/dokumentaatio/viikkoraportti6.md)**

# **Ohjelma käyttöohje**

## **Asennus ja käyttö**

1. Lataa Githubin Release
    - Release sisältää opetukseen tarvittavan datan
        - Käytössä seuraavat sävellajit: A, C, G
        - Kansioon F on kerätty kaikki opetusdata, jota voi myös testata
        - Kansiossa B on yksikkötestien käyttämä testidata

2. Asenna riippuvuudet komennolla:

`poetry install`

3. Käynnistä algoritmi ajamalla *sovellus/src* -kansiossa seuraava komento:

`poetry shell`

jonka jälkeen

`python main.py`

tai suoraan Sovellus-kansiossa, mikäli sovellus ei toimi:

`python src/main.py`

## **Huomioita tämän hetken versiosta:**

1. Ohjelma tuottaa opetusdatan perusteella toistettavan ja kuunneltavan midi-tiedoston. Tiedosto luodaan opetusdatana käytettyyn kansioon.

2. **[Esimerkkimusiikkia (algoritmin tuottamia)](https://github.com/vtonteri/Algoritmisovellus/tree/master/data/musiikki)**