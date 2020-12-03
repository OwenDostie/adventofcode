f = open("day3.txt").read().split()
gw = len(f[0]) # grid width
i = 0 # index off current position
ct = 0 # number off trees

for r in f: # for each row
    if r[i%gw] == "#": ct += 1
    i += 3
    
print("Part one:", ct)

product = 1
for x,y in [[1,1], [3,1], [5,1], [7,1], [1,2]]:
    i = 0 # index of charaacter
    ct = 0
    for r in f:
        if i%1 == 0:
            if r[int(i%gw)] == "#":
                ct += 1
        i += x/y
    print(ct)
    product *= ct

print("Part two:", product)