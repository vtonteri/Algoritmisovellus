class TrieSolmu:
    def __init__(self):
        self.lapsi = {}
        self.on_viimeinen = False


class TrieRakenne:
    def __init__(self):
        self.juuri = TrieSolmu()

    def lisaa_nuotit(self, nuotit: str):
        solmu = self.juuri
        for nuotti in nuotit:
            if nuotti not in solmu.lapsi:
                solmu.lapsi[nuotti] = TrieSolmu()
            solmu = solmu.lapsi[nuotti]
        solmu.on_viimeinen = True 

    def etsi_nuotit(self, etsittavat_nuotit: str) -> bool:
        solmu = self.juuri
        for nuotti in etsittavat_nuotit:
            if nuotti not in solmu.lapsi:
                return False
            solmu = solmu.lapsi[nuotti]
        return solmu.on_viimeinen
    
    