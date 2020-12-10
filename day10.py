f = list(map(int, open('day10.txt').read().split()))
f.append(max(f)+3); f.append(0)
f = sorted(f)

diffs = {}
p = f[0]
for i in f[1:]:
    diffs[i-p] = diffs.get(i-p,0) + 1
    p = i
print('Part one:',diffs[3]*diffs[1])

n_paths = {0:1}
for i in f[1:]:
    n_paths[i] = n_paths.get(i-1,0) + n_paths.get(i-2,0) + n_paths.get(i-3,0)
print(n_paths[max(f)])