R, C, M = map(int, input().split(' '))

dx = [0, -1, 1, 0, 0]
dy = [0, 0, 0, 1, -1]

eaten_shark = set()

shark_arr = [[0] * (C + 1) for _ in range(R + 1)]
shark_info = {}


def get_fish(column):
    weight = 0
    #print(shark_arr[3][1])
    for i in range(1, R + 1):
        if shark_arr[i][column]:
            weight = shark_arr[i][column]
            shark_arr[i][column] = 0
            eaten_shark.add(weight)
            break
    return weight


def move_fish(r, c, s, d, z):

    if d == 1:
        r -= s % ((R - 1) * 2)
    elif d == 2:
        r += s % ((R - 1) * 2)
    elif d == 3:
        c += s % ((C - 1) * 2)
    elif d == 4:
        c -= s % ((C - 1) * 2)

    while True:
        if 0 < r <= R and 0 < c <= C:
            break
        else:
            if r <= 0:
                r = 2 - r
                d = 2
            elif r > R:
                r = R - (r - R)
                d = 1
            elif c <= 0:
                c = 2 - c
                d = 3
            elif c > C:
                c = C - (c - C)
                d = 4

    shark_info[z] = [r, c, s, d]
    origin_shark = shark_arr[r][c]
    if origin_shark:
        #print("origin_shark", origin_shark)
        if z > origin_shark:
            eaten_shark.add(origin_shark)
            #print("eaten origin", origin_shark)
            shark_arr[r][c] = z
        else:
            eaten_shark.add(z)
            #print("eaten", z)
    else:
        shark_arr[r][c] = z


for _ in range(M):
    r, c, s, d, z = map(int, input().split(' '))
    shark_arr[r][c] = z
    shark_info[z] = [r, c, s, d]

answer = 0

#print(shark_info)

for column in range(1, C + 1):
    answer += get_fish(column)
    shark_arr = [[0] * (C + 1) for _ in range(R + 1)]
    for size, shark_information in shark_info.items():
        if size not in eaten_shark:
            r, c, s, d = shark_information
            move_fish(r, c, s, d, size)


print(answer)
