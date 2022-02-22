from collections import deque
import sys

n, m = map(int, sys.stdin.readline().split(' '))
arr_map = []
for _ in range(n):
    arr_map.append(sys.stdin.readline().rstrip())

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs_map():
    visited = [[[0, 0] for _ in range(m)] for _ in range(n)]
    visited[0][0][1] = 1
    queue = deque([[0, 0, 1]])
    while queue:
        x, y, z = queue.popleft()
        if x == n - 1 and y == m - 1:
            return visited[x][y][z]
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if arr_map[nx][ny] == '1' and z == 1:
                    visited[nx][ny][0] = visited[x][y][1] + 1
                    queue.append([nx, ny, 0])
                elif arr_map[nx][ny] == '0' and visited[nx][ny][z] == 0:
                    visited[nx][ny][z] = visited[x][y][z] + 1
                    queue.append([nx, ny, z])
                # visited[nx][ny] = False
    return -1


print(bfs_map())
