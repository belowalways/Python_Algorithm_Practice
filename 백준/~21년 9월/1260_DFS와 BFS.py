from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for j in range(len(graph)):
    graph[j] = sorted(graph[j])

dfs_answer = []
bfs_answer = []

def dfs(graph, start, visited):
    visited[start] = True
    dfs_answer.append(start)
    for i in graph[start]:
        if not visited[i]:
            dfs(graph, i, visited)

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        vertix = queue.popleft()
        bfs_answer.append(vertix)
        for i in graph[vertix]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


dfs(graph, v, visited)
visited = [False] * (n+1)
bfs(graph, v, visited)

print(*dfs_answer)
print(*bfs_answer)
