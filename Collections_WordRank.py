'''
Sample Input

4
bcdef
abcdefg
bcde
bcdef
Sample Output

3
2 1 1
'''
from collections import OrderedDict
dct = OrderedDict()
for i in range(int(input())):
    word = input()
    dct.setdefault(word,0)
    dct[word]+=1

print(len(dct))
print(*dct.values())

