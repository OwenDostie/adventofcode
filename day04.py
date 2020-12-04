import re
f = open("day04.txt").read().replace("\n","-").split("--")

count = 0
for l in f:
    for field in ["byr","iyr","eyr","hgt","hcl","ecl","pid"]:
        if not field in l:
            count -= 1; break
    count += 1

print("Part 1:", count)
count = 0

for l in f:
    for field in ["byr:(19[2-9][0-9]|200[0-2])(\\s|$|-)",
    "iyr:(201[0-9]|2020)(\\s|$|-)",
    "eyr:(202[0-9]|2030)(\\s|$|-)",
    "hgt:(((1[5-8][0-9]|19[0-3])cm)|(59|6[0-9]|7[0-6])in)(\\s|$|-)",
    "hcl:#[0-9|a-f]{6}(\\s|$|-)",
    "ecl:(amb|blu|brn|gry|grn|hzl|oth)(\\s|$|-)",
    "pid:[0-9]{9}(\\s|$|-)"]:
        if re.search(field, l) is None:
            count -= 1; 
            #print(l,"\n","fault is --", field,"\n"); 
            break
    count += 1

print("Part 2:", count)