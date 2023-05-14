import os

class LuoOpetusData:

    """
    Luokka luo opetusdatan
    luokkaa kutsuttaessa luodaan muunnos-dict (Muunnetaan abc-notaation mukaiset merkinnät numeroiksi)
    """

    def __init__(self):
        self.muunnos_abc_numeroksi = {"C,": 0, "D,": 1, "E,": 2, "F,": 3, "G,": 4, "A,": 5, "B,": 6, "C": 7, "D": 8, "E": 9, "F": 10,
                                      "G": 11, "A":12, "B": 13, "c": 14, "d": 15, "e": 16, "f": 17, "g": 18, "a": 19, "b": 20, "c'":21,
                                      "d'": 22, "e'": 23, "f'": 24, "g'": 25, "a'": 26, "b'": 27}
        self.opetusdata_muunnettu = []
        self.muunnettu_savel_data = []

    def lue_ja_muunna_abc_testi_data(self):
        """
        Testiluokka, toteuttaa saman kuin lue_ja_muunna_abc, mutta käyttää pakotettuna testidataa.
        Vain testien käytössä.
        """

        try:
            os.chdir(r"..\data\data_testi")
            test_tiedostot = os.listdir(os.getcwd())
        except FileNotFoundError:
            pass
        try:
            os.chdir(r"data/data_testi")
            test_tiedostot = os.listdir(os.getcwd())
        except FileNotFoundError:
            print("Ei löydetty tiedostoa, lisää opetusdataa kansioon tai vaihda sävellajia")

        for tiedosto in test_tiedostot:
            try:
                with open(tiedosto, "r") as nuotit:
                    tarkistusbitti = 0
                    for rivi in nuotit:
                        for nuotti in rivi:
                            if nuotti == "\"":
                                tarkistusbitti += 1
                                if tarkistusbitti == 2:
                                    tarkistusbitti = 0
                            elif nuotti in self.muunnos_abc_numeroksi and tarkistusbitti == 0:
                                self.opetusdata_muunnettu.append(self.muunnos_abc_numeroksi[nuotti])
            except OSError:
                print("Ei löydetty tiedostoa, lisää opetusdataa kansioon tai vaihda sävellajia")

    def lue_ja_muunna_abc_data(self, savellaji: str):

        """
        Luokka lukee opetusdatan ja muuntaa sen numeroiksi.
        Args: käyttäjän valitsema sävellaji
        Sävellajin perusteella luetaan opetusdata-kansiosta opetusdata.
        Se tallennetaan self.opetusdata_muunnettu -listaksi.
        """
        try:
            os.chdir(f"..\data\opetusdata\{savellaji}")
            tiedostot = os.listdir(os.getcwd())
        except FileNotFoundError:
            pass
        try:
            os.chdir(f"data/opetusdata/{savellaji}")
            tiedostot = os.listdir(os.getcwd())
        except FileNotFoundError:
            print("Ei löydetty tiedostoa, lisää opetusdataa kansioon tai vaihda sävellajia")
        for tiedosto in tiedostot:
            try:
                with open(tiedosto, "r") as nuotit:
                    tarkistusbitti = 0
                    for rivi in nuotit:
                        for nuotti in rivi:
                            if nuotti == "\"":
                                tarkistusbitti += 1
                                if tarkistusbitti == 2:
                                    tarkistusbitti = 0
                            elif nuotti in self.muunnos_abc_numeroksi and tarkistusbitti == 0:
                                self.opetusdata_muunnettu.append(self.muunnos_abc_numeroksi[nuotti])
            except OSError as error:
                print("Ei löydetty tiedostoa, lisää opetusdataa kansioon tai vaihda sävellajia")

    def lue_ja_muunna_savel_data(self, muunnettavat_nuotit: list):

        """
        Luokka muuntaa numerot kirjaimiksi
        Args: muunnettavat_nuotit: list
        Palauttaa muunnetut nuotit listana
        """

        for i in muunnettavat_nuotit:
            for key, value in self.muunnos_abc_numeroksi.items():
                if i == value:
                    self.muunnettu_savel_data.append(key)
        return self.muunnettu_savel_data
