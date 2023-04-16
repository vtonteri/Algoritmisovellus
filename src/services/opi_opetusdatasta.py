"""g = {1: (2, 4), 2: (3, 6), 3: (10, 100)}


for value in g.values():
    print(f"tämä on key : {value[0]} {value[1]}")
    value[1] += 1


for i in range(2):
    g[i+1] = g[i+1]

print(g)
"""

"""
def rekursio(n: int, syotelista: list, apulista: list, x: int):

    if n == 0:
        return apulista
    
    for i in range(x):
        return None
"""

def opi(n, syotelista: list, apulista: list):

    for i in range(len(syotelista)-n+1):
        #print(syotelista[i])
        apulista = []
        for j in range(n):

            #print(syotelista[j+i])
            apulista.append(syotelista[j+i])
        print(apulista)    




if __name__ == "__main__":
   
   
    n = 10
    x = 0 
    syotelista = [i for i in range(21,100)]
    #syotelista = {"1": }
    apulista = []
    opi(n, syotelista, apulista)
    print(syotelista)

