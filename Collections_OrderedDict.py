'''
Sample Input

9
BANANA FRIES 12
POTATO CHIPS 30
APPLE JUICE 10
CANDY 5
APPLE JUICE 10
CANDY 5
CANDY 5
CANDY 5
POTATO CHIPS 30
Sample Output

BANANA FRIES 12
POTATO CHIPS 60
APPLE JUICE 20
CANDY 20
'''
from collections import OrderedDict
result = OrderedDict()
for i in range(int(input())):
    string = input().split()
    value = int(string[-1])
    string.pop(-1)
    string = ' '.join(string)
    if string in result:
        result[string] +=value
    else:
        result[string]=value
    
for i in result:
    print(i,result[i])
