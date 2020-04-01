'''
Sample Input

3 2
1 5 3
3 1
5 7
Sample Output

1
'''
m,n = map(int,input().split())
num_list = (map(int,input().split()))
A = set(map(int,input().split()))
B = set(map(int,input().split()))
happy = 0
for i in num_list:
    if i in A:
        happy+=1
    if i in B:
        happy-=1
print(happy)
