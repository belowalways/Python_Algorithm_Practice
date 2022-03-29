from collections import deque
from itertools import permutations

n, m, k = map(int, input().split())

origin_arr = [[]]
spin_list = []

for _ in range(n):
    origin_arr.append([0] + list(map(int, input().split())))

for _ in range(k):
    spin_list.append(tuple(map(int, input().split())))

for_seq = [i for i in range(k)]
perm_list = list(permutations(for_seq, k))

min_a = 999999999999999

for perm in perm_list:
    new_arr = []
    for origin in origin_arr:
        new_arr.append(origin[:])

    for p in perm:
        r, c, s = spin_list[p]

        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]

        for i in range(1, s + 1):
            queue = deque([])
            x, y = r - i, c - i
            queue.append(new_arr[x][y])
            for j in range(4):
                for _ in range(2 * i):
                    nx, ny = x + dx[j], y + dy[j]
                    queue.append(new_arr[x][y])
                    new_arr[x][y] = queue.popleft()
                    x, y = nx, ny
            new_arr[x][y] = queue.popleft()

    for o in range(1, n + 1):
        if sum(new_arr[o]) < min_a:
            min_a = sum(new_arr[o])

print(min_a)
