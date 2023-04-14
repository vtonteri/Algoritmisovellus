# **Viikkoraportti 3**

## Mitä olen tehnyt tällä viikolla?

- Toteutettu ABC-notaation lukeva ja Trie-rakenteeseen tiedon tallentava muunnin
    - Muuntimen toiminta:
        - Lukee .txt tiedoston (tällä hetkellä vielä vain yksi tiedosto)
        - Muuntaa notaation nuotit numeroiksi
        - Luo ja tallentaa tiedon Trie-rakenteeksi

- Toteutettu opi_opetusdatasta.py tiedostoon metodi opi, mikä huomioi halutun määrän Markovin ketjujen tiloja luodessaan Trie-rakenteen
    - Luokka pitää viimeistellä, perusrakenne on toimiva (ottaa syötteenä tilojen lukumäärän ja luo niiden perusteella apulistan, jota käytetään Trie-rakenteen luomiseen)

- Paranneltu Trie-rakenteesta tietyn kirjainyhdistelmän etsivää hakutoimintoa:
    - Virheellisten syötteiden käsittely lisätty, tämä on vielä kesken

- Testit:
    - Yksikkötestaus:

## Miten ohjelma on edistynyt?

- ABC-notaatiomuunnin toteutettu
- Yksikkötestaus aloitettu

## Mitä opin tällä viikolla / tänään?

- 

## Mikä jäi epäselväksi tai tuottanut vaikeuksia? Vastaa tähän kohtaan rehellisesti, koska saat tarvittaessa apua tämän kohdan perusteella.

- Tällä viikolla moni asia tuntui helpolta, joten tähän kohtaan ei ole raportoitavaa

## Mitä teen seuraavaksi?

- Aloitan koodaamaan painokertoimien perusteella uutta musiikkia tuottavan luokan
- Jatkan yksikkötestien kirjoittamista

## Käytetty tuntimäärä

- Arvio käytetystä ajasta: 8 h

Kumulatiivinen työajan seuranta:

| Viikko | Käytetty aika | Mitä tein |
| --- | --- | --- |
| 1 | 8 | Projektin alustaminen, tietorakenteen koodaus |
| 2 | 8 | Muuntimen pseudokoodin rakentaminen, Import-ongelman selvittely |
| 3 | 9 | Import-ongelman ratkaisu, Trie-rakenteen kehitys, abc-notaation selvittely |
| 4 | 8 | ABC-muuntimen koodaus, Trie-rakenteen hakutoiminnan kehitys, yksikkötestien kirjoittaminen |
| Yht | 33 |  |