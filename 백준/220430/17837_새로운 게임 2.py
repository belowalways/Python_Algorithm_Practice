n, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [0, 0, 0, -1, 1]
dy = [0, 1, -1, 0, 0]

horses = [[(-1, -1), -1]]

board_stack = [[[] for _ in range(n)] for _ in range(n)]

for i in range(1, k + 1):
    r, c, d = map(int, input().split())
    horses.append([(r - 1, c - 1), d])
    board_stack[r - 1][c - 1].append(i)

turn = 1
overflow = False
while True:
    for i in range(1, k + 1):
        x, y = horses[i][0]
        d = horses[i][1]
        # print(i, horses[i], board_stack[x][y])
        idx = board_stack[x][y].index(i)
        nx, ny = x + dx[d], y + dy[d]

        if not 0<=nx<n or not 0<=ny<n or board[nx][ny] == 2:
            if d % 2 == 1:
                d += 1
            else:
                d -= 1
            nx, ny = x + dx[d], y + dy[d]
            horses[i][1] = d
            if not 0<=nx<n or not 0<=ny<n or board[nx][ny] == 2:
                continue

        for tmp in range(idx, len(board_stack[x][y])):
            horses[board_stack[x][y][tmp]][0] = (nx, ny)

        if board[nx][ny] == 0:
            board_stack[nx][ny] += board_stack[x][y][idx:]
            board_stack[x][y] = board_stack[x][y][:idx]
        elif board[nx][ny] == 1:
            board_stack[nx][ny] += board_stack[x][y][idx:][::-1]
            board_stack[x][y] = board_stack[x][y][:idx]

        if len(board_stack[nx][ny]) >= 4:
            overflow = True
            break

    if overflow or turn == 1000:
        break

    turn += 1


if overflow:
    print(turn)
else:
    print(-1)
