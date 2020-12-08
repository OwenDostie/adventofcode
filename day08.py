import re
import sys
f = open('day08.txt').read().rstrip().split('\n')

# print(len(f))
# print(f[611])
# sys.exit()

cands = set()
for l,_ in enumerate(f):
    if re.search('nop|jmp', _):
        cands.add(l)

for swap in cands:
    print(swap)
    effs = set(); acc = 0; line = 0
    while True:
        if line == len(f):
            print('Part two: ', acc)
            sys.exit()
        if line in effs:
            print('Part one: ', acc); 
            break
        effs.add(line)
        if re.match('nop', f[line]):
            if line == swap:
                line += int(f[line][4:])        
        if re.match('acc', f[line]):
            acc += int(f[line][4:])
        if re.match('jmp', f[line]):
            if line != swap:
                line += int(f[line][4:])
                continue
        line += 1

