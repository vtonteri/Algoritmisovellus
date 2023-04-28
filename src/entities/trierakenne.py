from src.services.luo_opetusdata_abc import LuoOpetusData

class TrieSolmu:
    def __init__(self):
        self.lapsi = {}
        self.maara = 0
        self.on_viimeinen = False

    def __str__(self):
        return f"{self.lapsi.keys()}, {self.maara}, {self.on_viimeinen}"

class TrieRakenne:
    def __init__(self):
        self.juuri = TrieSolmu()

    def lisaa_nuotit(self, nuotit: str):
        solmu = self.juuri
        for nuotti in nuotit:
            if nuotti not in solmu.lapsi:
                solmu.lapsi[nuotti] = TrieSolmu()
            solmu = solmu.lapsi[nuotti]
            solmu.maara += 1
        solmu.on_viimeinen = True
        return solmu.on_viimeinen

    def etsi_nuotit(self, etsittavat_nuotit: str):
        solmu = self.juuri

        for nuotti in etsittavat_nuotit:
            if int(nuotti) not in solmu.lapsi:
                return False
            solmu = solmu.lapsi[int(nuotti)]
        return solmu

    def maarita_painokertoimet(nuotit, rakenne, savellaji):
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
