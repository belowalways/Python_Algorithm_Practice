import sys
sys.setrecursionlimit(10**6)

n = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    u, v = map(int, sys.stdin.readline().rstrip().split(' '))
    graph[u].append(v)
    graph[v].append(u)

global_node = -1
global_depth = -1


def find_length(start_node, depth, visited):
    global global_node
    global global_depth
    visited[start_node] = True
    if depth > global_depth:
        global_depth, global_node = depth, start_node
    for node in graph[start_node]:
        if not visited[node]:
            find_length(node, depth + 1, visited)


visited = [True] + [False] * n
find_length(1, 0, visited)
visited = [True] + [False] * n
global_depth = 0
find_length(global_node, 0, visited)
print(global_depth // 2 + global_depth % 2)
