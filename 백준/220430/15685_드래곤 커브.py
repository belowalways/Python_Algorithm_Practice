# 오른쪽 위 왼쪽 아래
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

n = int(input())

ans_arr = [[0] * 101 for _ in range(101)]
dp = [[0] * 101 for _ in range(101)]

for _ in range(n):
    x, y, d, g = map(int, input().split())
    ans_arr[y][x] = 1
    direction = [d]
    for _ in range(g):
        direction += [(a + 1) % 4 for a in direction[::-1]]
    for di in direction:
        x, y = x + dx[di], y + dy[di]
        ans_arr[y][x] = 1

count = 0

for i in range(101):
    for j in range(101):
        if i == 0 or j == 0:
            dp[i][j] = ans_arr[i][j]
        elif ans_arr[i][j] == 1:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
        if dp[i][j] >= 2:
            count += 1

print(count)







