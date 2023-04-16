# **Toteutusdokumentti**

## **Ohjelman yleisrakenne**

Ohjelma on jaettu toimintojensa osalta seuraaviin osakokonaisuuksiin:

- Entities:
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
                - Metodien toiminta:
                    - lisaa_nuotit:
                        - Ottaa syötteenä joko merkkijonon (str) tai listan (list). Pilkkoo merkkijonon yksittäisiin merkkeihin ja lisää ne TrieRakenteeseen
                        - Ei palauta mitään
                    - etsi_nuotit:
                        - Ottaa syötteenä joko merkkijonon (str) tai listan (list). Etsii merkkijonoa vastaavan TrieRakenteen ja palauttaa viimeisen solmun
                    - maarita_painokertoimet:
                        - Ottaa syötteenä joko merkkijonon (str) tai listan (list) sekä TrieRakenteen, josta halutaan etsiä tietoa. Kutsuu etsi_nuotit -metodia, joka palauttaa viimeisen nuotin jälkeen tulevien mahdollisten nuottien määrät. Tämän jälkeen määritetään jokaiselle nuotille painokerroin ja palautetaan dict, jossa key = nuotti ja value = painokerroin.
- Services:
    - Sisältää opetusdatan lukemiseen ja luomiseen tarvittavat luokat ja metodit
        - luo_opetusdata.py:
    - Sisältää opetusdatasta oppimiseen tarvittavat luokat ja metodit
    - Sisältää opetusdatan perusteella luotavaan musiikkitiedostoon tarvittavat luokat ja metodit


## **Saavutetut aika- ja tilavaativuudet (m.m. O-analyysit pseudokoodista)**


## **Suorituskyky- ja O-analyysivertailu (mikäli työ vertailupainotteinen)**


## **Työn mahdolliset puutteet ja parannusehdotukset**


## **Lähteet**

    - Introduction to algorithms, Third edition
    - Understanding machine learning : from theory to algorithms
    - Data Analysis with Python
    - Machine learning algorithms : popular algorithms for data science and machine learning
    - Advanced machine learning with Python : solve challenging data science problems by mastering cutting-edge machine learning techniques in Python
    - https://en.wikipedia.org/wiki/Algorithmic_composition
    - https://en.wikipedia.org/wiki/Markov_chain
    - https://abcnotation.com/
    