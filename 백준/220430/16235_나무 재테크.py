n, m, k = map(int, input().split())

tree_arr = [[[] for _ in range(n)] for _ in range(n)]
g_arr = [[5] * n for _ in range(n)]
a_arr = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 1, 1, -1, -1, -1, 0, 0]
dy = [1, 0, -1, 1, 0, -1, 1, -1]

for _ in range(m):
    x, y, z = map(int, input().split())
    tree_arr[x-1][y-1].append(z)

for _ in range(k):
    for x in range(n):
        for y in range(n):
            if tree_arr[x][y]:
                tree_arr[x][y].sort()
                tmp_arr = []
                tmp_value = 0
                for tree in tree_arr[x][y]:
                    if g_arr[x][y] >= tree:
                        g_arr[x][y] -= tree
                        tmp_arr.append(tree + 1)
                    else:
                        tmp_value += tree // 2
                tree_arr[x][y] = tmp_arr
                g_arr[x][y] += tmp_value
    for x in range(n):
        for y in range(n):
            if tree_arr[x][y]:
                for tree in tree_arr[x][y]:
                    if tree % 5 == 0:
                        for d in range(8):
                            nx, ny = x + dx[d], y + dy[d]
                            if 0 <= nx < n and 0 <= ny < n:
                                tree_arr[nx][ny].append(1)
    for x in range(n):
        for y in range(n):
            g_arr[x][y] += a_arr[x][y]

answer = 0
for x in range(n):
    for y in range(n):
        answer += len(tree_arr[x][y])
print(answer)

'''from collections import defaultdict
n, m, k = map(int, input().split())

dx = [-1, -1, -1, 1, 1, 1, 0, 0]
dy = [1, 0, -1, 1, -1, 0, 1, -1]

a_arr = [list(map(int, input().split())) for _ in range(n)]
ground_arr = [[5] * n for _ in range(n)]
tree_dict = defaultdict(list)

for _ in range(m):
    x, y, z = map(int, input().split())
    x, y = x-1, y-1
    tree_dict[(x, y)] += [z]

for _ in range(k):
    for (x, y) in tree_dict:
        tree_list = tree_dict[(x, y)]
        tree_list.sort()
        grow_tree_list = []
        energy = 0
        for tree in tree_list:
            if ground_arr[x][y] >= tree:
                ground_arr[x][y] -= tree
                grow_tree_list.append(tree + 1)
            else:
                energy += tree // 2
        tree_dict[(x, y)] = grow_tree_list
    next_tree_dict = defaultdict(list)
    for (x, y) in tree_dict:
        tree_list = tree_dict[(x, y)]
        for tree in tree_list:
            if tree % 5 == 0 and tree // 5 >= 1:
                for i in range(8):
                    nx, ny = x + dx[i], y + dy[i]
                    if 0<=nx<n and 0<=ny<n:
                        next_tree_dict[(nx, ny)] += [1]
    for (x, y) in next_tree_dict:
        tree_dict[(x, y)] += next_tree_dict[(x, y)]
    for i in range(n):
        for j in range(n):
            ground_arr[i][j] += a_arr[i][j]
    print(tree_dict)

answer = 0
for tree_list in tree_dict.values():
    answer += len(tree_list)
print(answer)
'''