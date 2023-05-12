from src.services.luo_opetusdata_abc import LuoOpetusData

class TrieSolmu:
    """
    Luokka luo olion TrieSolmu.
    Solmu sisältää 
    - solmuun liittyvät lapset dictionaryssa
    - määrän, kuinka monta kertaa solmun läpi on lisätty nuotteja
    - tiedon, onko solmu viimeinen
    """
    def __init__(self):
        self.lapsi = {}
        self.maara = 0
        self.on_viimeinen = False

    def __str__(self):
        return f"{self.lapsi.keys()}, {self.maara}, {self.on_viimeinen}"

class TrieRakenne:
    """
    Luokka luo Trie-tietorakenteen.
    Luokkaa kutsuttaessa, se luo juuren (TrieSolmu), johon lisätään muut solmut
    """
    def __init__(self):
        self.juuri = TrieSolmu()

    def lisaa_nuotit(self, nuotit: str):
        """
        Luokka lisää TrieRakenteeseen tietoa, eli uusia solmuja
        Args: nuotit; voi olla joko lista tai merkkijono. Pituus on määritetty sen mukaan kuinka monella markovin ketjun tilalla halutaan musiikkia tehdä
        Palauttaa tiedon, mikäli solmu on viimeinen
        """
        solmu = self.juuri
        for nuotti in nuotit:
            if nuotti not in solmu.lapsi:
                solmu.lapsi[nuotti] = TrieSolmu()
            solmu = solmu.lapsi[nuotti]
            solmu.maara += 1
        solmu.on_viimeinen = True
        return solmu.on_viimeinen

    def etsi_nuotit(self, etsittavat_nuotit: str):
        """
        Luokka etsii TrieRakenteesta nuotit
        Args: nuotit; voi olla lista tai merkkijono
        Palauttaa joko False (jos ei ole lapsia) tai solmun, mikäli ei ollut viimeinen (eli dict, määrä ja on.viimeinen)
        """
        solmu = self.juuri

        for nuotti in etsittavat_nuotit:
            if int(nuotti) not in solmu.lapsi:
                return False
            solmu = solmu.lapsi[int(nuotti)]
        return solmu

    def maarita_painokertoimet(nuotit, rakenne, savellaji):
        """
        Luokka määrittää painokertoimet etsittäville nuoteille.
        Args: etsittävät nuotit, tietorakenne ja sävellaji
        Palauttaa dict, missä seuraavat nuotit ja painokertoimet. Mikäli viimeinen nuotti, niin palauttaa valitun sävellajin ja painokerroin 1.0
        """
        vika = rakenne.etsi_nuotit(nuotit)
        summa = 0
        seuraava_nuotti = {}
        if vika is False:
            return {LuoOpetusData().muunnos_abc_numeroksi[savellaji]: 1.0}
        for key in vika.lapsi.keys():
            summa += vika.lapsi[key].maara
            seuraava_nuotti[key] = vika.lapsi[key].maara
        apusumma = 0
        for key in seuraava_nuotti.keys():
            seuraava_nuotti[key] = apusumma + seuraava_nuotti[key]/summa
            apusumma = seuraava_nuotti[key]
        return seuraava_nuotti
