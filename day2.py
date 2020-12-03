import re

f = filter(None,open("day2.txt").read().split("\n"))

count1 = 0; count2 = 0
for line in f:
    # part one
    l = re.split("-|:| ",line)
    cc = 0
    for c in l[4]:
        cc += (l[2] == c)
    count1 += (cc >= int(l[0]) and cc <= int(l[1]))
    
    # part two
    print(int(l[0])-1, int(l[1])-1, l)
    print(l[4][int(l[0])-1],l[4][int(l[1])-1],l[2])
    count2 += (l[4][int(l[0])-1] == l[2])^(l[4][int(l[1])-1] == l[2])  

print("Part one:", count1)
print("Part two:", count2)