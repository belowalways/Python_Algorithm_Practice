row_len = 0
col_len = 0

dir_order_list = []

grid = ["SL", "LR"]

def cycle(start_x, start_y, start_dir, grid):
    global dir_order_list

    # 위 오른쪽 아래 왼쪽
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    dir_order = [start_dir]
    x = start_x
    y = start_y
    dir = start_dir

    while True:
        if grid[x][y] == "R":
            dir += 1
        elif grid[x][y] == "L":
            dir -= 1

        if dir < 0:
            dir = 3
        elif dir > 3:
            dir = 0

        dir_order.append(dir)

        nx = x + dx[dir]
        ny = y + dy[dir]

        if nx > row_len:
            nx = 0
        elif nx < 0:
            nx = row_len - 1
        if ny > col_len:
            ny = 0
        elif ny < 0:
            ny = col_len - 1

        x, y = nx, ny

        if dir == start_dir and x == start_x and y == start_y:
            break

    dir_order_list.append(dir_order)


def solution(grid):
    global dir_order_list
    global row_len
    global col_len

    row_len = len(grid)
    col_len = len(grid[0])

    for i in range(col_len):
        x, y = 0, i
        dir = 2
        cycle(x, y, dir, grid)

    for i in range(col_len):
        x, y = -1, i
        dir = 0
        cycle(x, y, dir, grid)

    for j in range(row_len):
        x, y = j, 0
        dir = 1
        cycle(x, y, dir, grid)

    for j in range(row_len):
        x, y = j, -1
        dir = 3
        cycle(x, y, dir, grid)

    answer = []

    for dir_order in dir_order_list:
        answer.append(len(dir_order))

    return answer


solution(grid)

# visited 3차원 ;

# 2206번

