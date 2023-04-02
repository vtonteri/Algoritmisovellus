from random import random

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

    def etsi_nuotit(self, etsittavat_nuotit: str) -> bool:
        solmu = self.juuri

        for nuotti in etsittavat_nuotit:
            if nuotti not in solmu.lapsi:
                return False   
            #print(solmu.lapsi[nuotti].maara)         
            solmu = solmu.lapsi[nuotti]
            
            #print(f"{solmu} tämä on nuotti: {nuotti} {solmu.maara}")

        return solmu
    
    def maarita_painokertoimet(nuotit:str, rakenne):
        vika = rakenne.etsi_nuotit(nuotit)
    
        print(vika.lapsi.keys())
        summa = 0
        seuraava_nuotti = {}
        nuottien_maara = len(vika.lapsi)
        if not vika.lapsi:
                print("Tämä oli viimeinen nuotti, eikä sillä ole seuraajia. Valitse lopettava nuotti.")
        else:
            for key in vika.lapsi.keys():
                summa += vika.lapsi[key].maara
                seuraava_nuotti[key] = vika.lapsi[key].maara
        y=0
        for key in seuraava_nuotti.keys():
            seuraava_nuotti[key] = y + seuraava_nuotti[key]/summa
            y = seuraava_nuotti[key]

        kerroin = random()
        return seuraava_nuotti
    



if __name__ == '__main__':
    nuotit = "kala"
    liaa = "mies"
    f = "kalamies"
    s = "mieskala"
    t = "kalakala"
    y = "kalatyyppi"
    x = TrieRakenne()

    x.lisaa_nuotit(nuotit)
    x.lisaa_nuotit(liaa)
    x.lisaa_nuotit(f)
    x.lisaa_nuotit(s)
    x.lisaa_nuotit(t)
    x.lisaa_nuotit(y)
    x.lisaa_nuotit(y)
    x.lisaa_nuotit(y)
    x.lisaa_nuotit(y)
    x.lisaa_nuotit(["j","a","r"])
    print(TrieRakenne.maarita_painokertoimet("kala", x))