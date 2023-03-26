from entities.trie_rakenne import TrieRakenne

class LuoOpetusData():
    
    def __init__(self):
        self.opetusdata = TrieRakenne()

    
    def lue_ja_muunna_abc_data(self):

        f = open("data/opetusdata/a_testi_tiedosto.txt")

        for i in f:
            print(i)

       
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
        return None
    
    # ABC-tiedoston sisällöstä:
    # https://abcnotation.com/wiki/abc:standard:v2.1
    
    #Kommentointi:
    # |:DEF FED| % this is an end of line comment
    # % this is a comment line
    # DEF [r:and this is a remark] FED:|

if __name__ == "__main__":

    LuoOpetusData.lue_ja_muunna_abc_data()