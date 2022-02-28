from collections import deque

n, k, r = map(int, input().split(' '))

#[상, 하, 좌, 우]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

farm_list = [[[1, 1, 1, 1] for _ in range(n)] for _ in range(n)]
cow_list = []

count = 0

for _ in range(r):
    r1, c1, r2, c2 = map(int, input().split(' '))
    if r1 == r2:
        if c1 > c2:
            farm_list[r1][c1][2] = 0
            farm_list[r1][c2][3] = 0
        else:
            farm_list[r1][c2][2] = 0
            farm_list[r1][c1][3] = 0
    else:
        if r1 > r2:
            farm_list[r1][c1][1] = 0
            farm_list[r2][c1][0] = 0
        else:
            farm_list[r2][c1][1] = 0
            farm_list[r1][c1][0] = 0

for _ in range(k):
    x, y = map(int, input.split(' '))
    cow_list.append((x, y))

for cow in cow_list:
    tmp_cow_list = cow_list[:]
    visited = [[False * n] for _ in range(n)]
    queue = deque(cow)
    while queue:
        x, y = queue.popleft()
        visited[x][y] = True
        for bridge in farm_list[x][y]:
            if bridge == 1:
                nx, ny = x + dx[bridge], y + dy[bridge]
                if not visited[nx][ny]:
                    queue.append((nx, ny))

    count += len(tmp_cow_list)
