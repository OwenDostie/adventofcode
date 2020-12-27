import re
import pandas as pd
from math import ceil
f = open("owen/owen.csv").read().replace("\"","").replace(",","").split()

###### PART ONE ######
ct = 0
for r in range(1,len(f)-1):
    for c in range(1,len(f[0])-1):
        ct += f[r][c] not in [f[r-1][c],f[r][c-1]] and f[r][c] != "w"
print("Part one:", ct)

###### PART TWO ######
d = {}; dd = {}; threadSaved = 0
for r in range(1,len(f)-1):
    for c in range(1,len(f[0])-1):
        if f[r][c] not in [f[r-1][c],f[r][c-1]]:
            if f[r][c] not in d:
                d[f[r][c]] = {}
            l = 0
            while f[r][c+l] == f[r][c]: l += 1
            d[f[r][c]][l] = d[f[r][c]].get(l,0) + 1
            dd[f[r][c]] = dd.get(f[r][c],0) + l ** 2
            threadSaved += (l-1)*l*2

print("Part two:",''.join([str(ceil(dd[_]/40)).zfill(2) for _ in list('roygbiv')]))

###### PART THREE ######
w = len(f[0]) - 2; h = len(f) - 2
print("Part three:",(w+1) * h + (h+1) * w - threadSaved)

