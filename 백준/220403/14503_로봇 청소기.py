import sys
n, m = map(int, sys.stdin.readline().rstrip().split(' '))
r, c, d = map(int, sys.stdin.readline().rstrip().split(' '))
clean_arr = []
visited = [[False] * m for _ in range(n)]

for _ in range(n):
    clean_arr.append(list(map(int, sys.stdin.readline().rstrip().split(' '))))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

x, y = r, c
i = d
count = 0
visited[x][y] = True
clean_cnt = 1

while True:
    nd = i - 1
    if nd < 0:
        nd = 4 + nd
    nx, ny = x + dx[nd], y + dy[nd]
    if (not visited[nx][ny]) and (clean_arr[nx][ny] == 0):
        i = nd
        x, y = nx, ny
        visited[x][y] = True
        clean_cnt += 1
        count = 0
    else:
        if count != 4:
            i = nd
            count += 1
        else:
            nx, ny = x - dx[i], y - dy[i]
            if clean_arr[nx][ny] == 1:
                break
            x, y = nx, ny
            count = 0


print(clean_cnt)








