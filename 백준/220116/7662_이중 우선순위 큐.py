import heapq

n = int(input())

for _ in range(n):
    k = int(input())
    lst = []
    heapq.heapify(lst)
    for _ in range(n):
        a, b = input().split()
        if a == 'I':
            heapq.heappush(lst, int(b))
        elif a == 'D':
            if b == '1':
                -heapq.heappop(lst)
            elif b == '-1':
                heapq.heappop(lst)
    print(heapq.heappop(lst))

'''from queue import PriorityQueue

n = int(input())

for _ in range(n):
    k = int(input())
    que = PriorityQueue()
    for _ in range(n):
        a, b = input().split()
        if a == 'I':
            que.put(int(b))
        elif a == 'D':
            if b == '1':
                que.get
            elif b == '-1':
                heapq.heappop(lst)'''



