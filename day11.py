import numpy as np

f = '''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''
print(type(f),f)
f = f.translate(str.maketrans({'L':'1','.':'0'}))
print(type(f),f)
f = np.fromstring(f,sep='\n')
print(type(f),f)



asdf
seatmap = np.array(list(map(int,f.translate(str.maketrans({'L':'1','.':'0'})).split())))
print(seatmap.shape)
print(seatmap[2:])
sdfsdf
z = np.zeros_like(seatmap)
z[1:,:] += seatmap[:-1,:]
print(z)


asdfasdf.sdf
seatmap = np.array(list(map(int,open('day11.txt').read().translate(str.maketrans({'L':'1','.':'0'})).split())))

z = np.zeros_like(seatmap)
z[1:,0] += seatmap[:-1,0]
print()
# print(np.pad(seatmap,((0,0),(0,0)),mode='constant'))


f = '''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''
print(f)