from collections import deque

n = int(input())
answer = [[] for _ in range(n)]
visited = [0] * n

for i in range(n-1):
    temp = list(map(int, input().split()))

    answer[temp[0]-1].append(temp[1])
    answer[temp[1]-1].append(temp[0])

print(answer)


'''def bfs(queue, visited):
    while queue:'''

from collections import deque, Counter

n = int(input())
answer = [[] for _ in range(n + 1)]
visited = [0] * (n + 1)

for i in range(n-1):
    temp = list(map(int, input().split()))

    answer[temp[0]].append(temp[1])
    answer[temp[1]].append(temp[0])


sequence = list(map(int, input().split()))

i = sequence.pop()
queue = deque[i]

visited[i] = 1
tmp = sequence.pop()
if answer[i].count(tmp) == 1:
    i = tmp
    visited[i] = 1


print(answer)




