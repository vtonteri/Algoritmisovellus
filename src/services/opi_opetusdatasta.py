class OpiDatasta:
    
    def __init__(self):
        self.apulista = []

    def opi(self, tilojen_maara, syotelista: list):
        for i in range(len(syotelista)-tilojen_maara+1):
            for j in range(tilojen_maara):
                self.apulista.append(syotelista[j+tilojen_maara])
            
            self.apulista = []
        return self.apulista    
    
if __name__ == "__main__":
   
   
    n = 10
    x = OpiDatasta() 
    syotelista = [i for i in range(21,100)]
    #syotelista = {"1": }
    apulista = []
    print(x.opi(n, syotelista))

