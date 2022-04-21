import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
practice_arr = [list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n)]


dx = [0, 0, -1, -1, -1, 0, 1, 1, 1]
dy = [0, -1, -1, 0, 1, 1, 1, 0, -1]


def move(x, y, d, s):
    s %= n
    nx, ny = x + s * dx[d], y + s * dy[d]
    if nx >= n:
        nx -= n
    elif nx < 0:
        nx += n
    if ny >= n:
        ny -= n
    elif ny < 0:
        ny += n
    return nx, ny


now_cloud = [(n-1, 0), (n-1, 1), (n-2, 0), (n-2, 1)]
for _ in range(m):
    d, s = map(int, input().split())
    prev_cloud = []
    for x, y in now_cloud:
        nx, ny = move(x, y, d, s)
        prev_cloud.append((nx, ny))
        practice_arr[nx][ny] += 1

    visited = [[False] * n for _ in range(n)]

    for i in range(len(prev_cloud)):
        x, y = prev_cloud[i]
        visited[x][y] = True
        for d in (2, 4, 6, 8): # copy
            nnx, nny = x + dx[d], y + dy[d]
            if 0 <= nnx < n and 0 <= nny < n:
                if practice_arr[nnx][nny] > 0:
                    practice_arr[x][y] += 1


    now_cloud = []
    for i in range(n):
        for j in range(n):
            if practice_arr[i][j] >= 2 and not visited[i][j]:
                now_cloud.append((i, j))
                practice_arr[i][j] -= 2

answer = 0
for p in practice_arr:
    answer += sum(p)
print(answer)
