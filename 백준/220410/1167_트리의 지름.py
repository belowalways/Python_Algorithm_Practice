v = int(input())

tree = [[] for _ in range(v + 1)]

for _ in range(v):
    length_arr = list(map(int, input().split(' ')))
    start_node = length_arr[0]
    for i in range(1, len(length_arr) - 1, 2):
        tree[start_node].append((length_arr[i], length_arr[i+1]))

#print(tree)
global_depth = -1
global_node = -1

def find_length(start_node, depth, visited):
    global global_node
    global global_depth
    visited[start_node] = True
    if depth > global_depth:
        global_depth, global_node = depth, start_node
    for node, length in tree[start_node]:
        if not visited[node]:
            find_length(node, depth + length, visited)


visited = [True] + [False] * v
find_length(1, 0, visited)
visited = [True] + [False] * v
global_depth = 0
find_length(global_node, 0, visited)
print(global_depth)


