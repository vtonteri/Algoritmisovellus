from src.entities.trierakenne import TrieRakenne

class OpiDatasta:

    def __init__(self):
        self.apulista = []
        self.opetusdata = TrieRakenne()

    def opi(self, tilojen_maara, syotelista: list):
        for i in range(len(syotelista)-tilojen_maara+1):
            for j in range(tilojen_maara):
                self.apulista.append(syotelista[i + j])
            self.opetusdata.lisaa_nuotit(self.apulista)
            self.apulista = []
        return self.opetusdata
