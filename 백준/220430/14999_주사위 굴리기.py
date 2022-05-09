n, m, x, y, k = map(int, input().split())
map_arr = [list(map(int, input().split())) for _ in range(n)]

dice_height = [0, 0, 0, 0]
dice_width = [0, 0, 0]

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]


move_command = list(map(int, input().split()))
dice = [0] * 6

for move in move_command:
    nx, ny = x + dx[move], y + dy[move]
    if 0<=nx<n and 0<=ny<m:
        x, y = nx, ny
    else:
        continue

    if move == 1: # 동
        dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    elif move == 2: # 서
        dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    elif move == 3: # 북
        dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]
    elif move == 4: # 남
        dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]

    if map_arr[x][y] == 0:
        map_arr[x][y] = dice[5]
    else:
        dice[5] = map_arr[x][y]
        map_arr[x][y] = 0

    print(dice[0])

