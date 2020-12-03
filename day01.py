from itertools import combinations
f = open("day01.txt","r")
f = list(map(int, f.read().splitlines()))

seeking = set()

def findPair(sumsTo):
    for n in f:
        if n in seeking: return (n * (sumsTo - n))
        seeking.add(sumsTo - n)

def findTriplet():
    for i1 in range(len(f)):
        subTotal = 2020-f[i1]
        seeking = set()
        for i2 in range(i1, len(f)):
            if f[i2] in seeking:
                return f[i1]*f[i2]*(subTotal - f[i2])
            seeking.add(subTotal - f[i2])

print("Part one:", findPair(2020))
print("Part two:", findTriplet())

print("Using itertools combinations:")
for combo in combinations(f,3):
    if sum(combo) == 2020:
        print(combo[0]*combo[1]*combo[2])
        break