import sys

r1, c1, r2, c2 = map(int, sys.stdin.readline().split())

row = r2 - r1 + 1
col = c2 - c1 + 1

snail_list = [[0] * col for _ in range(row)]

max_level = max(abs(r1), abs(c1), abs(r2), abs(c2))

for level in range(max_level - 50, max_level + 1):
    spot = [level, level]
    value = (2 * level + 1) ** 2

# if r1 <=

now = 1

# 오른쪽 위 왼쪽 아래
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

max_snail = max(snail_list[0][0], snail_list[row][0], snail_list[0][col], snail_list[row][col])

length = len(str(max_snail))

'''for r in range(row):
    for c in range(col):
        print(str(snail_list[r][c]).rjust(length), end= ' ')
    print()'''

print_format = "{0:>" + str(length + 1) + "}"

for row in snail_list:
    row_print = ""
    for val in row:
        row_print += print_format.format(str(val))
        if row_print[0] == " ":
            sys.stdout.write(row_print[1:] + "\n")
        else:
            sys.stdout.write(row_print + "\n")

