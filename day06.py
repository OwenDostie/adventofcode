import string
import sys
f = open('day06.txt').read().rstrip().split('\n\n')

print(f)

# part one
t = 0
S = set(string.ascii_lowercase)

for l in f:
    s = set(l)
    t += len(set.intersection(S,s))
print("Part one:", t)

t = 0
for l in f:
    S = set(string.ascii_lowercase)
    for i in l.split('\n'):
        S = set.intersection(S,set(i))
    print('\n',l)
    print(S, len(S),"dddd")
    t += len(S)

print("Part two:", t)
# print(t)