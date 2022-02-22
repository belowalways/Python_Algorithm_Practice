from collections import deque
import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split(' '))
arr_map = []
for _ in range(n):
    arr_map.append(input())

visited = [[False] * m for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

min_length = 999999999

def dfs_map(x, y, length, power, visited):
    global min_length

    if x == n-1 and y == m-1 and min_length > length:
        min_length = length
        return

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0<=nx<n and 0<=ny<m:
            if visited[nx][ny] == False:
                if arr_map[nx][ny] == '0':
                    visited[nx][ny] = True
                    dfs_map(nx, ny, length + 1, power, visited)
                    visited[nx][ny] = False
                elif power:
                    visited[nx][ny] = True
                    dfs_map(nx, ny, length + 1, False, visited)
                    visited[nx][ny] = False


dfs_map(0, 0, 1, True, visited)

if min_length == 999999999:
    print(-1)
else:
    print(min_length)
