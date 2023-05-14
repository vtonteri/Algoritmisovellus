# **Testausdokumentti**

## **Yleistä**

Ohjelmalle on kirjoitettu yksikkötestit seuraaville luokille:

- TrieRakenne
- LuoOpetusData
- OpiDatasta

Yksikkötestien lisäksi ohjelman virheiden etsinnässä on käytetty Pylintiä. Tällä hetkellä Pylint:n hyvyysarvo on 9.41 / 10 .pylintrc on kopioitu Ohjelmistotekniikka-kurssin materiaalista ja sitä on hieman muokattu. 

Ohjelmasta on tarkoituksella jätetty pois LuoUusiMidiTiedosto- sekä LuoUusiKappale-luokan testaus. Tämä on sovittu kurssin vastuuopettajan kanssa, sillä Midi-tiedoston luonti ei ole kurssin osaamistavoitteiden näkökulmasta keskeisessä roolissa. 

**Testauksessa on keskitytty opetusdatan luonnin ja Trie-rakenteen oikeellisuuden ja toiminnan varmistamiseen.**

Haaraumakattavuus on 74 %

![haaraumakattavuus](https://github.com/vtonteri/Algoritmisovellus/blob/master/dokumentaatio/haaraumakattavuus.jpg)

luo_opetusdata_abc -luokan kattavuus on raportissa 55 %. Tähän on syynä se että kyseisen luokan sisällä on luotu erillinen testaukseen suunniteltu metodi. Metodi hakee testidatan eri kansiosta, kuin oikean opetusdatan hakeva metodi. Oikean opetusdatan ja testausdatan noutavat metodit ovat muutoin samat, paitsi, että niissä on eri tiedostopolku.

## **Minkälaisilla syötteillä testaus tehtiin (vertailupainotteisissa töissä tärkeää)?**

- Yksikkötestejä varten luotiin testidataa. Testidata oli osin yksinkertaista (alle kymmenen merkkiä sisältäviä listoja) tai pidempi abc-notaatiolla tehty kappale (noin 100 merkkiä)
- Yksinkertaisten syötteiden avulla oli mahdollista testata ja todentaa luokkien ja metodien toiminta. Mikäli testidata olisi ollut kompleksista, olisi esimerkiksi painokertoimien määrittäminen ollut haastavaa
- Yksinkertaiset syötteet testaavat kuitenkin metodien toimintaa, koska ne on valittu testitilanteisiin sopiviksi

## **Miten testit voidaan toistaa?**

Testit voidaan ajaa käyttäen seuraavaa komentoa poetryn avulla:

`poetry run invoke test`

Mikäli käyttäjällä on Windows-käyttöjärjestelmä, testit voidaan suorittaa seuraavalla komennolla:

`pytest src`

Ohjelman toiminnan empiirisen testauksen tulosten esittäminen graafisessa muodossa.