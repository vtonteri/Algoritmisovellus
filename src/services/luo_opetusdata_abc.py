from entities.trierakenne import TrieRakenne, TrieSolmu

class LuoOpetusData:
    
    def __init__(self):
        self.muunnos_abc_numeroksi = {"C,": 0, "D,": 1, "E,": 2, "F,": 3, "G,": 4, "A,": 5, "B,": 6, "C": 7, "D": 8, "E": 9, "F": 10, "G": 11, "A":12, "B": 13, "c": 14, "d": 15, "e": 16, 
                                      "f": 17, "g": 18, "a": 19, "b": 20, "c'":21, "d'": 22, "e'": 23, "f'": 24, "g'": 25, "a'": 26, "b'": 27}
        self.opetusdata_muunnettu = []

        #self.rakenne = TrieRakenne()

    def lue_ja_muunna_abc_data(self):

        f = open("data/opetusdata/G/G_data_1.txt")

        for i in f:
            for j in i:
                if j in self.muunnos_abc_numeroksi:
                    self.opetusdata_muunnettu.append(self.muunnos_abc_numeroksi[j])

        print(self.opetusdata_muunnettu)



       
        #Kuvaus pseudokoodina:
        # Alusta tyhjä dictionary
        # Kovakoodattuna pitää olla muunnin nuoteista numeroiksi: tähän käy dictionary, jossa key on nuotti ja key:tä vastaava item on numero
        # For-loopin sisällä toteutetaan seuraava:
            # 1. avaa polun ../data/opetusdata alta aakkosissa ensimmäisenä oleva abc-tiedosto
            # 2. Toisen for-loopin sisällä toteutetaan seuraava:
                # 3. Alusta dictionaryyn uusi lista seuraavalla järjestysnumerolla 
                # 3. Käy tiedoston sisältö läpi seuraavasti:
                    # 4. Ignooraa alkumerkit (tiedosto on valittu oikeasta sävellajista)
                    # 5. Kun löydät merkkiyhdistelmän |: --> aloita lukeminen ja tallentaminen
                    # 6. lue merkki kerrallaan nuotit, muunna nuotti muunnin-dict:stä löytyvän key-item parin perusteella numeroksi
                    # 7. Tallenna muunnettu merkki self.opetusdata -tietorakenteeseen

    
    # ABC-tiedoston sisällöstä:
    # https://abcnotation.com/wiki/abc:standard:v2.1
    
    #Kommentointi:
    # |:DEF FED| % this is an end of line comment
    # % this is a comment line
    # DEF [r:and this is a remark] FED:|