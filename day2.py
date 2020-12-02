import re
f = filter(None,open("day2.txt").read().split("\n"))

count = 0
for line in f:
    l = re.split("-|:| ",line)
    cc = 0
    for c in l[4]:
        cc += (l[2] == c)
    count += (cc >= int(l[0]) and cc <= int(l[1]))

print("Part one:", count)
count = 0
print("hi")
for line in f:
    l = re.split("-|:| ",line)
    cc = 0
    print(l[int(l[0])-1],l[int(l[1])-1],l[2])
    count += (l[int(l[0])-1] == l[2])^(l[int(l[1])-1] == l[2])

print("Part two:", count)