g = {1: (2, 4), 2: (3, 6), 3: (10, 100)}


for value in g.values():
    print(f"tämä on key : {value[0]} {value[1]}")
    value[1] += 1


for i in range(2):
    g[i+1] = g[i+1]

print(g)
