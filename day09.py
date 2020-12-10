import itertools as it
import sys
f = open('day09.txt').read().rstrip().split()
f = list(map(int,f))

l = f[:25]; slot = 0

for i in f[25:]:
    if i not in set(map(sum,list(it.combinations(l,2)))):
        print('Part one:', i)
        break
    l[slot] = i
    slot = (slot + 1)%25

for left in range(25,len(f)):
    for right in range(left + 1,len(f)):
        s = sum(f[left:right])
        #print(left,right,s)
        if s >= 20874512:
            if s == 20874512:
                print('Part two:',min(f[left:right])+ max(f[left:right]))
                sys.exit()
            break