import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().rstrip().split(' '))
    graph[u].append(v)
    graph[v].append(u)

save_distance = [0] * (n + 1)

queue = deque([])

for i in range(1, n + 1):
    if len(graph[i]) == 1:
        queue.append(i)

while queue:
    city = queue.popleft()
    for next_city in graph[city]:
        if city in graph[next_city]:
            graph[next_city].remove(city)
        if save_distance[next_city] < save_distance[city] + 1:
            save_distance[next_city] = save_distance[city] + 1
            queue.append(next_city)

print(save_distance)
