g = {1: 2, 2: 3, 3: 10}

summa = sum(g.values())

for key in g.keys():
    print(f"{g[key] / summa} tämä on key : {key}")

print(summa)

for i in range(2):
    g[i+1] = g[i+1] + 10

print(g)
