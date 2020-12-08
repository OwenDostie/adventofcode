import re

f = open('day07.txt').read().rstrip().split('\n')

# f = '''light red bags contain 1 bright white bag, 2 muted yellow bags.
# dark orange bags contain 3 bright white bags, 4 muted yellow bags.
# bright white bags contain 1 shiny gold bag.
# muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
# shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
# dark olive bags contain 3 faded blue bags, 4 dotted black bags.
# vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
# faded blue bags contain no other bags.
# dotted black bags contain no other bags.'''.split('\n')

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

S = set()
def childrenBags(bags):
    l = []
    bags = '('+'|'.join(bags)+')'
    for row in f:
        m = re.search("(.*)s contain .*" + bags, row)
        if m:
            print(row, m.group(1), bags, '\n--------\n')
            l.append(m.group(1))
            S.add(m.group(1))
    if l:
        parentBags(l)

print('Part two:', len(S))