import os

class LuoOpetusData:
    
    def __init__(self):
        self.muunnos_abc_numeroksi = {"C,": 0, "D,": 1, "E,": 2, "F,": 3, "G,": 4, "A,": 5, "B,": 6, "C": 7, "D": 8, "E": 9, "F": 10, "G": 11, "A":12, "B": 13, "c": 14, "d": 15, "e": 16, 
                                      "f": 17, "g": 18, "a": 19, "b": 20, "c'":21, "d'": 22, "e'": 23, "f'": 24, "g'": 25, "a'": 26, "b'": 27}
        self.opetusdata_muunnettu = []

    def lue_ja_muunna_abc_data(self, savellaji: str):

        os.chdir(f"data/opetusdata/{savellaji}")
        tiedostot = os.listdir(os.getcwd())
        print(tiedostot)

        for tiedosto in tiedostot:
            try:
                with open(tiedosto, "r") as nuotit:
                    for rivi in nuotit:
                        for nuotti in rivi:
                            if nuotti in self.muunnos_abc_numeroksi:
                                self.opetusdata_muunnettu.append(self.muunnos_abc_numeroksi[nuotti])
            except OSError as error:
                print("Ei löydetty tiedostoa, lisää opetusdataa kansioon tai vaihda sävellajia")

        print(self.opetusdata_muunnettu)
