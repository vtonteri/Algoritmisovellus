from src.entities.trierakenne import TrieRakenne

class OpiDatasta:

    """
    Luokka luo Trierakenteen opetusdatan perusteella
    """

    def __init__(self):
        self.apulista = []
        self.opetusdata = TrieRakenne()

    def opi(self, tilojen_maara, syotelista: list):
        """
        Metodi lisää self.opetusdata -rakenteeseen syötelistalla olevat merkkijonot tilojen määrän mukaisesti.
        Metodi palauttaa kyseisen Trierakenteen.
        """

        for i in range(len(syotelista)-tilojen_maara+1):
            for j in range(tilojen_maara):
                self.apulista.append(syotelista[i + j])
            self.opetusdata.lisaa_nuotit(self.apulista)
            self.apulista = []
        return self.opetusdata
