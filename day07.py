import re

f = open('day07.txt').read().rstrip().split('\n')

# f = '''shiny gold bags contain 2 dark red bags.
# dark red bags contain 2 dark orange bags, 2 dark green bags, 5 purple bags.
# purple bags conntain no other bags.
# dark orange bags contain 2 dark yellow bags.
# dark yellow bags contain 2 dark green bags.
# dark green bags contain 2 dark blue bags.
# dark blue bags contain 2 dark violet bags.
# dark violet bags contain no other bags'''.split('\n')

S = set()
def parentBags(bags):
    l = []
    bags = '('+'|'.join(bags)+')'
    for row in f:
        m = re.search("(.*)s contain .*" + bags, row)
        if m:
            #print(row, m.group(1), bags, '\n--------\n')
            l.append(m.group(1))
            S.add(m.group(1))
    if l:
        parentBags(l)

parentBags(['shiny gold bag'])
print('Part one:', len(S))

print(f)
def childrenBags(bags):
    ct = 0
    bags = '('+'|'.join(bags)+')'
    for row in f:
        if not re.match(bags + "s contain", row): continue
        m = re.findall("\d .*? bag", row)
        if m:
            #print(m)
            for i in m:
                ct += int(i[:1]) * childrenBags([i[2:]])
            ct += 1
        else:
            # print(row)
            return 1
    return ct

#print(childrenBags(['mirrored blue bag']))
print('Part two:', childrenBags(['shiny gold bag']) - 1)

# 1+    2 + 2() + 