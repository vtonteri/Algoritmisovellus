# **Toteutusdokumentti**

## **Ohjelman yleisrakenne**

Ohjelma on jaettu toimintojensa osalta seuraaviin osakokonaisuuksiin:

- **Entities:**
    - Sisältää Trie-tietorakenteen konstruointiin ja hakemiseen tarvittavat luokat ja metodit
        - trierakenne.py sisältää luokat TrieSolmu ja TrieRakenne
            - TrieSolmu:
                - On Trie-tietorakenteen yksi solmu
                - Solmussa on dictionary, määrä (int) sekä muuttuja on_viimeinen (bool)
            - TrieRakenne:
                - Sisältää metodit
                    - lisaa_nuotit
                    - etsi_nuotit
                    - maarita_painokertoimet
                - Luotaessa TrieRakenne, luodaan sille juuri, joka on TrieSolmu
                
- **Services:**
    - Sisältää opetusdatan lukemiseen ja luomiseen tarvittavat luokat ja metodit
        - luo_opetusdata.py sisältää luokan LuoOpetusData
            - Luokka sisältää abc-notaation muuntamiseen tarvittavan dictionaryn, johon on määritetty nuotteja vastaavat lukuarvot. Opetusdata sisältää numeroita, jotka vastaavat tiettyjä nuotteja.
            - Luokka sisältää metodit, 
                - lue_ja_muunna_abc_data 
                - lue_ja_muunna_savel_data
                - lue_ja_muunna_abc_testi_data
        - opi_opetusdatasta.py
            - Luokka sisältää metodit
                - opi
        - tee_uusi_midi_tiedosto.py
            - Luokka sisältää metodit
                - luo_uusi_midi_tiedosto
                - sakeisto
                - kertosae
                - bridge
                - melodia
        - luo_uusi_kappale.py
            - Luokka sisältää metodit
                - luo_uusi_kappale

        
    - Sisältää opetusdatasta oppimiseen tarvittavat luokat ja metodit
    - Sisältää opetusdatan perusteella luotavaan musiikkitiedostoon tarvittavat luokat ja metodit

## **Ohjelman toiminta pähkinänkuoressa**

1. Main.py kysytään käyttäjän haluama sävellaji sekä Markovin ketjujen määrä. Tämän jälkeen
2. Kutsutaan näillä syötteillä LuoUusiKappale-luokkaa, joka toimii seuraavalla tavalla:
3. Luodaan opetusdata kutsumalla LuoOpetusData-luokkaa (valittu sävellaji ja tilojen määrä), jonka jälkeen
4. Muunnetaan opetusdata kirjaimista numeroiksi käsittelyn helpottamiseksi, jonka jälkeen
5. Opitaan datasta kutsumalla OpiDatasta-luokkaa, eli luodaan TrieRakenne. Rakenteen luomisen jälkeen
6. Kutsutaan luotua TrieRakennetta ja määritetään uutta kappaletta varten seuraavat nuotit:
    - Seuraava nuotti määritetään tarkastamalla TrieRakenteesta valittujen Markovin tilojen määrän pituinen nuottijono, jonka jälkeen etsitään mahdolliset seuraajat ja arvotaan seuraaja painokertoimien ja satunnaisluvun avulla
7. Sävelkierron luomisen jälkeen muunnetaan numerot takaisin nuoteiksi
8. Tämän jälkeen kutsutaan TeeUusiMidiTiedosto -luokkaa
9. TeeUusiMidiTiedosto-luokan metodin "luo_uusi_midi_tiedosto" kutsumisella luodaan ja tallennetaan uusi kappale 


## **Saavutetut aika- ja tilavaativuudet (m.m. O-analyysit pseudokoodista)**

Algoritmin aikavaativuus määrittyy tietorakenteen luomisen ja sieltä tiedon haun perusteella. Trie-rakenteen tila- ja aikavaativuus on kirjallisuuden mukaan:

- Tilavaativuus: O(n)
- Aikavaativuus:
    - O(log(n))
        - Lisääminen, poistaminen ja tiedon haku

## **Työn mahdolliset puutteet ja parannusehdotukset**

Työn puutteina voidaan mainita seuraavat asiat:
- Algoritmi ei hae automaattisesti kappaleita mistään
    - Käyttäjän pitää noutaa kappaleet haluamastaan paikasta ja muuntaa data opetusdata-kansiossa olevien tekstitiedostojen osoittamaan muotoon
- Algoritmi ei erottele tekstitiedoston sisällön perusteella mihin sävellajiin opetusdata kuuluu
    - Opetusdata pitää manuaalisesti jaotella sävellajien mukaisiin kansioihin
- Algoritmi luo kappaleen käytetyn sävellajin mukaiseen opetusdata-kansioon
    - Kappale pitää poistaa tai siirtää toiseen kansioon, jotta uuden kappaleen luonti samalla sävellajilla onnistuu



## **Lähteet**

    - Introduction to algorithms, Third edition
    - Understanding machine learning : from theory to algorithms
    - Data Analysis with Python
    - Machine learning algorithms : popular algorithms for data science and machine learning
    - Advanced machine learning with Python : solve challenging data science problems by mastering cutting-edge machine learning techniques in Python
    - https://en.wikipedia.org/wiki/Algorithmic_composition
    - https://en.wikipedia.org/wiki/Markov_chain
    - https://abcnotation.com/
    