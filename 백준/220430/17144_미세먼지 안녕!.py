r, c, t = map(int, input().split())
room_arr = [list(map(int, input().split())) for _ in range(r)]
air_fresher = -1

# 위 오른쪽 아래 왼쪽
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(r):
    if room_arr[i][0] == -1:
        air_fresher = i
        break

for _ in range(t):
    move_dust_arr = [[0] * c for _ in range(r)]
    # 확산
    for i in range(r):
        for j in range(c):
            if room_arr[i][j] > 0:
                dust_amount = room_arr[i][j] // 5
                count = 0
                for d in range(4):
                    ni, nj = i + dx[d], j + dy[d]
                    if 0<=ni<r and 0<=nj<c:
                        if room_arr[ni][nj] != -1:
                            count += 1
                            move_dust_arr[ni][nj] += dust_amount
                room_arr[i][j] -= dust_amount * count
    # 확산 반영
    for i in range(r):
        for j in range(c):
            room_arr[i][j] += move_dust_arr[i][j]

    # 순환
    tmp_x = air_fresher - 1
    tmp_y = 0
    tmp_d = 0
    while tmp_x != air_fresher or tmp_y != 1:
        nx, ny = tmp_x + dx[tmp_d], tmp_y + dy[tmp_d]
        if 0<=nx<=air_fresher and 0<=ny<c:
            room_arr[tmp_x][tmp_y] = room_arr[nx][ny]
            tmp_x, tmp_y = nx, ny
        else:
            tmp_d += 1
            continue
    room_arr[air_fresher][1] = 0
    # 순환
    tmp_x = air_fresher + 2
    tmp_y = 0
    tmp_d = 2
    while tmp_x != air_fresher + 1 or tmp_y != 1:
        nx, ny = tmp_x + dx[tmp_d], tmp_y + dy[tmp_d]
        if air_fresher<nx<r and 0<=ny<c:
            room_arr[tmp_x][tmp_y] = room_arr[nx][ny]
            tmp_x, tmp_y = nx, ny
        else:
            tmp_d -= 1
            if tmp_d == -1:
                tmp_d = 3
            continue
    room_arr[air_fresher + 1][1] = 0

answer = 2
for room in room_arr:
    answer += sum(room)
print(answer)
