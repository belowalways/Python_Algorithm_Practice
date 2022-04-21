from collections import deque

n = int(input())
k = int(input())

# apple = 1 snake = 2
board_arr = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(k):
    x, y = map(int, input().split())
    board_arr[x][y] = 1

# 위 오른쪽 아래 왼쪽
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

l = int(input())
dir_arr = deque([])
for _ in range(l):
    str_t, str_d = input(). split()
    t = int(str_t)
    d = 0
    if str_d == 'L':
        d = -1
    elif str_d == 'D':
        d = 1
    dir_arr.append((t, d))

snake_x = 1
snake_y = 1
snake_queue = deque([(1, 1)])
snake_dir = 1
board_arr[1][1] = 2
now_t = 1
next_change_dir_t, next_change_dir_d = dir_arr.popleft()

while True:
    snake_x, snake_y = snake_x + dx[snake_dir], snake_y + dy[snake_dir]
    if not 0 < snake_x <= n or not 0 < snake_y <= n:
        break
    elif board_arr[snake_x][snake_y] == 2:
        break

    if board_arr[snake_x][snake_y] == 0:
        tail_x, tail_y = snake_queue.popleft()
        board_arr[tail_x][tail_y] = 0

    board_arr[snake_x][snake_y] = 2
    snake_queue.append((snake_x, snake_y))

    if now_t == next_change_dir_t:
        snake_dir += next_change_dir_d
        if snake_dir < 0:
            snake_dir += 4
        elif snake_dir >= 4:
            snake_dir -= 4
        if len(dir_arr) > 0:
            next_change_dir_t, next_change_dir_d = dir_arr.popleft()
        else:
            next_change_dir_t, next_change_dir_d = 0, 0

    now_t += 1

print(now_t)

