import sys

m, n = map(int, sys.stdin.readline().rstrip().split(' '))
k = int(input())
map_list = []
for _ in range(m):
    map_list.append(sys.stdin.readline().rstrip())

sum_list = [[[0, 0, 0] for _ in range(n)] for _ in range(m)]

for y in range(m):
    for x in range(n):
        if x != 0:
            for i in range(3):
                sum_list[y][x][i] += sum_list[y][x - 1][i]
        tmp_map = map_list[y][x]
        if tmp_map == 'J':
            sum_list[y][x][0] += 1
        elif tmp_map == 'O':
            sum_list[y][x][1] += 1
        elif tmp_map == 'I':
            sum_list[y][x][2] += 1

for y in range(m):
    for x in range(n):
        if y != 0:
            for i in range(3):
                sum_list[y][x][i] += sum_list[y-1][x][i]

dot_list = []

for _ in range(k):
    a, b, c, d = map(int, sys.stdin.readline().rstrip().split(' '))
    a, b, c, d = a-1, b-1, c-1, d-1
    dot_list.append((a, b, c, d))

for dot in dot_list:
    tmp_list = []
    a, b, c, d = dot
    for i in range(3):
        tmp_sum = sum_list[c][d][i]
        if a > 0 and b > 0:
            tmp_sum += sum_list[a - 1][b - 1][i]
        if b > 0:
            tmp_sum -= sum_list[c][b - 1][i]
        if a > 0:
            tmp_sum -= sum_list[a - 1][d][i]
        tmp_list.append(tmp_sum)
    print(*tmp_list)


