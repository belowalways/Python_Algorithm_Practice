from collections import deque

n, l, r = map(int, input().split())
ground_arr = []
for _ in range(n):
    ground_arr.append(list(map(int, input().split())))

# 위 오른쪽 아래 왼쪽
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
next_visit = deque([(0, 0)])
visited = [[False] * n for _ in range(n)]

queue = deque([])


def bfs(x, y):
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        if visited[x][y]:
            continue
        visited[x][y] = True
        tmp_value = ground_arr[x][y]
        group_location_arr.append((x, y))
        group_value_arr.append(tmp_value)
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if not 0 <= nx < n or not 0 <= ny < n:
                continue
            elif visited[nx][ny]:
                continue
            gap_value = tmp_value - ground_arr[nx][ny]
            if gap_value < 0:
                gap_value = -gap_value
            if l <= gap_value <= r:
                queue.append((nx, ny))


count = 0

while True:
    group_location_arr = []
    group_value_arr = []
    visited = [[False] * n for _ in range(n)]
    is_moved = False
    for i in range(n):
        for j in range(n):
            if not visited[i][j]:
                group_location_arr = []
                group_value_arr = []
                bfs(i, j)
                if len(group_location_arr) > 1:
                    avg_value = sum(group_value_arr) // len(group_location_arr)
                    for (x, y) in group_location_arr:
                        if not is_moved:
                            if ground_arr[x][y] != avg_value:
                                is_moved = True
                        ground_arr[x][y] = avg_value
    if not is_moved:
        print(count)
        break
    count += 1
