import sys

def abs(x):
    if x > 0:
        return x
    else:
        return -x

r1, c1, r2, c2 = map(int, sys.stdin.readline().split())

row = r2 - r1 + 1
col = c2 - c1 + 1

min_level = min(abs(r1), abs(r2), abs(c1), abs(c2))
max_level = max(abs(r1), abs(r2), abs(c1), abs(c2))

snail_list = [[0] * col for _ in range(row)]

now = 1
x, y = 0, 0
i = 2

# 오른쪽 위 왼쪽 아래
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
pos = [-1, -1]
# print(snail_list)

for level in range(max_level-50, max_level + 1):

    pos[0] = level
    pos[1] = level

    if level == 0:
        snail_list[-r1][-c1] = 1
        continue

    move_list = [2] * (2 * level) + [1] * (2 * level) + [0] * (2*level) + [3] * (2*level)
    val = (2 * level + 1) ** 2
    # print(val, move_list)
    for j in move_list:
        # print(val, snail_list)
        if r1 <= pos[0] <= r2 and c1 <= pos[1] <= c2:
            snail_list[pos[0]-r1][pos[1]-c1] = val
        val -= 1
        nx = pos[0] + dx[j]
        ny = pos[1] + dy[j]
        pos = [nx, ny]


max_snail = max(snail_list[0][0], snail_list[row-1][0], snail_list[0][col-1], snail_list[row-1][col-1])

length = len(str(max_snail))

# print(snail_list)

for r in range(row):
    for c in range(col):
        print(str(snail_list[r][c]).rjust(length), end= ' ')
    print()

'''print_format = "{0:>" + str(length+1) + "}"

for row in snail_list:
    row_print = ""
    for val in row:
        row_print += print_format.format(str(val))
        if row_print[0] == " ":
            sys.stdout.write(row_print[1:] + "\n")
        else:
            sys.stdout.write(row_print + "\n")'''