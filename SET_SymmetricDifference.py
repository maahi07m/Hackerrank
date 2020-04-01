'''
Sample Input

4
2 4 5 9
4
2 4 11 12
Sample Output

5
9
11
12
'''
m=int(input())
set1 = set(map(int,input().split()))
n=int(input())
set2= set(map(int,input().split()))
list1=[]
list1.extend(list(set2.difference(set1)))
list1.extend(list(set1.difference(set2)))
list1.sort()
[print(i) for i in list1]
