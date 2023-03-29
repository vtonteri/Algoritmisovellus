class TrieSolmu:
    def __init__(self):
        self.lapsi = {}
        self.maara = 0
        self.on_viimeinen = False
    
    def __str__(self):
        return str(self.lapsi.keys())


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
            #solmu[1] += 1
            #solmu[nuotti][1] += 1
        solmu.on_viimeinen = True 

    def etsi_nuotit(self, etsittavat_nuotit: str) -> bool:
        solmu = self.juuri
        summa = 0
        

        for key in solmu.lapsi:
            print(solmu.lapsi[key].maara)


        for nuotti in etsittavat_nuotit:
            if nuotti not in solmu.lapsi:
                return False            
            solmu = solmu.lapsi[nuotti]
            print(f"{solmu} tämä on nuotti: {nuotti} {solmu.maara}")

        return solmu.on_viimeinen, solmu.maara, solmu.lapsi.keys()
    

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

    print(x.etsi_nuotit("tyyppi"))
