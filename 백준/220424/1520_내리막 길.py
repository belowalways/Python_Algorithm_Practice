import sys
sys.setrecursionlimit(10 ** 6)

m, n = map(int, input().split())
map_arr = []
dp = [[-1] * n for _ in range(m)]
dp[0][0] = 1

for _ in range(m):
    map_arr.append(list(map(int, input().split())))

# 위 오른쪽 아래 왼쪽
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def find_route(i, j):
    if dp[i][j] >= 0:
        return dp[i][j]
    dp[i][j] = 0
    for d in range(4):
        ni, nj = i + dx[d], j + dy[d]
        if 0 <= ni < m and 0 <= nj < n:
            if map_arr[ni][nj] > map_arr[i][j]:
                dp[i][j] += find_route(ni, nj)
    return dp[i][j]


print(find_route(m-1, n-1))

