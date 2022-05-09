import math
from collections import deque

n = int(input())
space = [list(map(int, input().split())) for _ in range(n)]
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

# x, y, size, count, last_t, t
baby_shark = (-1, -1)
baby_shark_size = 2
eaten_fish_count = 0
answer = 0

for x in range(n):
    for y in range(n):
        if space[x][y] == 9:
            space[x][y] = 0
            baby_shark = (x, y)
            break


def bfs(baby_shark):
    global answer
    global eaten_fish_count
    global baby_shark_size

    queue = deque([baby_shark])
    visited = [[0] * n for _ in range(n)]
    t = math.inf
    min_x, min_y = baby_shark

    while queue:
        x, y = queue.popleft()
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and space[nx][ny] <= baby_shark_size:
                if 0 < space[nx][ny] < baby_shark_size:
                    if visited[x][y] < t:
                        t = visited[x][y]
                        min_x, min_y = nx, ny
                    elif visited[x][y] == t:
                        if nx < min_x:
                            min_x, min_y = nx, ny
                        elif nx == min_x:
                            min_y = min(ny, min_y)
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

    if (min_x, min_y) == baby_shark:
        print(answer)
        return

    space[min_x][min_y] = 0
    eaten_fish_count += 1
    if eaten_fish_count == baby_shark_size:
        eaten_fish_count = 0
        baby_shark_size += 1

    answer += t + 1
    bfs((min_x, min_y))


bfs(baby_shark)
