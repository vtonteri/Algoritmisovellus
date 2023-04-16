# **Viikkoraportti 4**

## Mitä olen tehnyt tällä viikolla?

- Toteutettu ABC-notaation lukeva ja Trie-rakenteeseen tiedon tallentava muunnin
    - Muuntimen toiminta:
        - Lukee kaikki .txt tiedostot tällä hetkellä vain opetusdata/G -kansiosta 
        - Muuntaa notaation nuotit numeroiksi
        - Luo ja tallentaa tiedon Trie-rakenteeksi

- Toteutettu opi_opetusdatasta.py tiedostoon metodi opi, mikä huomioi halutun määrän Markovin ketjujen tiloja luodessaan Trie-rakenteen
    - Luokka pitää viimeistellä, perusrakenne on toimiva (ottaa syötteenä tilojen lukumäärän ja luo niiden perusteella apulistan, jota käytetään Trie-rakenteen luomiseen)

- Paranneltu Trie-rakenteesta tietyn kirjainyhdistelmän etsivää hakutoimintoa:
    - Virheellisten syötteiden käsittely lisätty, tämä on vielä kesken

- Testit:
    - Yksikkötestaus laahaa pahasti jäljessä

## Miten ohjelma on edistynyt?

- ABC-notaatiomuunnin toteutettu
- Markovin ketjujen tilojen määrän huomioon ottava opetusmetodi luotu
- Yksikkötestaus aloitettu

## Mitä opin tällä viikolla / tänään?

- Tiedostojen lukeminen
- Eri metodien ja luokkien käyttäminen keskenään ja yhteen taidot syventyivät huomattavasti

## Mikä jäi epäselväksi tai tuottanut vaikeuksia? Vastaa tähän kohtaan rehellisesti, koska saat tarvittaessa apua tämän kohdan perusteella.

- Yksikkötestien kirjoittaminen laahaa tällä hetkellä todella pahasti jäljessä. Jostain syystä en ole saanut aikaiseksi niiden kirjoittamista. Ne eivät ole periaatteessa vaikeita ja olenkin testannut koodin toimivuutta osana kehitystä, nyt ne pitäisi vain saada kirjoitettua testiluokiksi.

## Mitä teen seuraavaksi?

- Aloitan koodaamaan painokertoimien perusteella uutta musiikkia tuottavan luokan
- Jatkan yksikkötestien kirjoittamista

## Käytetty tuntimäärä

- Arvio käytetystä ajasta: 9 h

Kumulatiivinen työajan seuranta:

| Viikko | Käytetty aika | Mitä tein |
| --- | --- | --- |
| 1 | 8 | Projektin alustaminen, tietorakenteen koodaus |
| 2 | 8 | Muuntimen pseudokoodin rakentaminen, Import-ongelman selvittely |
| 3 | 9 | Import-ongelman ratkaisu, Trie-rakenteen kehitys, abc-notaation selvittely |
| 4 | 9 | ABC-muuntimen koodaus, Trie-rakenteen hakutoiminnan kehitys, yksikkötestien kirjoittaminen |
| Yht | 34 |  |