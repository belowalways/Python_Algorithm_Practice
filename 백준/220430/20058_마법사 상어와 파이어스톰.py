from collections import deque

n, q = map(int, input().split())
ice_length = 2 ** n
ice_arr = [list(map(int, input().split())) for _ in range(ice_length)]
stage = list(map(int, input().split()))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

def rotate(x_start, y_start, length):
    half_length = length // 2

    # 1 2
    # 4 3
    # 4번을 저장해서 1번에 줄거면
    # 3 -> 4 2 -> 3 1 -> 2
    # 이런 순서대로 복붙을 해야 하니까

    locations = [(x_start, y_start), (x_start, y_start + half_length), (x_start + half_length, y_start + half_length), (x_start + half_length, y_start)]
    saved_arr = [[0] * half_length for _ in range(half_length)]

    for i in range(x_start + half_length, x_start + length):
        for j in range(y_start, y_start + half_length):
            saved_arr[(j - y_start)][half_length - (i - (x_start + half_length)) - 1] = ice_arr[i][j]

    for idx in range(2, -1, -1):
        prev_x, prev_y = locations[idx]
        next_x, next_y = locations[idx + 1]
        for i in range(prev_x, prev_x + half_length):
            for j in range(prev_y, prev_y + half_length):
                ice_arr[next_x + j - prev_y][next_y + half_length - (i - prev_x) - 1] = ice_arr[i][j]

    for i in range(half_length):
        for j in range(half_length):
            ice_arr[x_start + i][y_start + j] = saved_arr[i][j]


for s in stage:
    # 2 ** n / 2 ** s ** 2 개 만큼의 격자 생김
    # 한 줄에 2 ** (n-s) 개 격자, 격자의 크기는 2 ** s
    for x_start in range(0, ice_length, 2 ** s):
        for y_start in range(0, ice_length, 2 ** s):
            rotate(x_start, y_start, 2 ** s)
    melt_location = []
    for x in range(ice_length):
        for y in range(ice_length):
            count = 0
            for d in range(4):
                nx, ny = x + dx[d], y + dy[d]
                if 0<=nx<ice_length and 0<=ny<ice_length and ice_arr[nx][ny] != 0:
                    count += 1
            if count < 3 and ice_arr[x][y] > 0:
                melt_location.append((x, y))
    for (x, y) in melt_location:
        if ice_arr[x][y] > 0:
            ice_arr[x][y] -= 1


visited = [[0] * ice_length for _ in range(ice_length)]
max_chunk = 0
ice_sum = 0

for x in range(ice_length):
    for y in range(ice_length):
        chunk_count = 0
        if visited[x][y] or ice_arr[x][y] == 0:
            continue
        queue = deque([(x, y)])
        visited[x][y] = 1

        while queue:
            i, j = queue.popleft()
            ice_sum += ice_arr[i][j]
            chunk_count += 1
            for d in range(4):
                ni, nj = i + dx[d], j + dy[d]
                if 0<=ni<ice_length and 0<=nj<ice_length and not visited[ni][nj] and ice_arr[ni][nj] != 0:
                    visited[ni][nj] = 1
                    queue.append((ni, nj))
        max_chunk = max(max_chunk, chunk_count)

print(ice_sum)
print(max_chunk)
