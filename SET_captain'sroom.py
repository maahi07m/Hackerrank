'''
Sample Input

5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 
Sample Output

8
'''
k = int(input())
rooms = list(map(int,input().split()))
room_set = set(rooms)
room_set = [int(i) for i in room_set]
print((sum((room_set)*k)-sum(rooms))//(k-1))
