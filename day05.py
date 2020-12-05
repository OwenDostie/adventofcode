f = open("day05.txt").read().replace("B","1").replace("F","0").replace("R","1").replace("L","0").split()

# min 45, max 953
m = 0
mm = 100
dd = [0]*1024
# didnt realize u could represent seat as 10 digit binary number till afterwards oops
for l in f:
    t = int("0b" + l[0:7],2)*8 + int("0b" + l[7:10],2)
    m = max(m,t)
    mm = min(mm,t)
    dd[t] = 1

print("Part one: ", m)
for v in range(45,953):
    if dd[v] == 0:
        print("Part two: ", v)