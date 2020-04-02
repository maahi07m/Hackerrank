'''
Sample Input

5 2
a
a
b
a
b
a
b
Sample Output

1 2 4
3 5
'''
from collections import defaultdict

d=defaultdict(list)

m,n = map(int,input().split())

for i in range(m):
    d[input()].append(str(i+1))

for i in range(n):
    print(' '.join(map(str, d[input()])) or -1)
