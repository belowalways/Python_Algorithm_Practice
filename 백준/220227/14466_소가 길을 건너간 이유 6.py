from collections import deque
import sys

n, k, r = map(int, input().split(' '))

#[상, 하, 좌, 우]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

farm_list = [[[False] * 4 for _ in range(n)] for _ in range(n)]
cow_list = [[False] * n for _ in range(n)]
cow_tuple = []

answer = 0

for _ in range(r):
    r1, c1, r2, c2 = map(int, sys.stdin.readline().rstrip().split(' '))
    r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1
    if r1 == r2:
        if c1 < c2:
            farm_list[r1][c1][3] = True
            farm_list[r1][c2][2] = True
        else:
            farm_list[r1][c1][2] = True
            farm_list[r1][c2][3] = True
    else:
        if r1 < r2:
            farm_list[r1][c1][1] = True
            farm_list[r2][c1][0] = True
        else:
            farm_list[r1][c1][0] = True
            farm_list[r2][c1][1] = True

for _ in range(k):
    x, y = map(int, sys.stdin.readline().rstrip().split(' '))
    x, y = x - 1, y - 1
    cow_list[x][y] = True
    cow_tuple.append((x, y))

for cow in cow_tuple:
    visited = [[False] * n for _ in range(n)]
    queue = deque([cow])
    visited[cow[0]][cow[1]] = True
    count = 0
    while queue:
        x, y = queue.popleft()
        if cow_list[x][y]:
            count += 1
        for i in range(4):
            if not farm_list[x][y][i]:
                nx, ny = x + dx[i], y + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if not visited[nx][ny]:
                        queue.append((nx, ny))
                        visited[nx][ny] = True

    answer += k - count

print(int(answer/2))
