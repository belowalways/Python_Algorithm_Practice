import math
from collections import deque
n, m = map(int, input().split())
lab_arr = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def combination(arr, n):
    length = len(arr)
    answer = []

    def dfs(visited, idx):
        if len(visited) == n:
            answer.append(visited[:])
            return

        for i in range(idx, length):
            visited.append(arr[i])
            dfs(visited, i + 1)
            visited.pop()

    dfs([], 0)
    return answer


virus_location_arr = []

for i in range(n):
    for j in range(n):
        if lab_arr[i][j] == 2:
            virus_location_arr.append((i, j))

virus_location_comb = combination(virus_location_arr, m)


def check(map):
    for m in map:
        if 0 in m:
            return False
    return True


def bfs(start, lab_arr):
    visited = [[0] * n for _ in range(n)]
    lab_arr = [row[:] for row in lab_arr]
    queue = deque()

    for s in start:
        queue.append((s[0], s[1], 0))

    last_change = 0

    while queue:
        x, y, cnt = queue.popleft()
        visited[x][y] = 1
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and lab_arr[nx][ny] != 1:
                visited[nx][ny] = 1
                if lab_arr[nx][ny] == 0:
                    lab_arr[nx][ny] = 2
                    last_change = cnt + 1
                queue.append((nx, ny, cnt + 1))

    if check(lab_arr):
        return last_change
    else:
        return -1


ans = math.inf

for comb in virus_location_comb:
    value = bfs(comb, lab_arr)
    if value != -1 and value < ans:
        ans = value

if ans == math.inf:
    print(-1)
else:
    print(ans)
