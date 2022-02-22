import sys

n = int(sys.stdin.readline())

seat_list = [[0] * n for _ in range(n)]
empty_seat = [[0] * n for _ in range(n)]

# 3차원 리스트로 주변 좌석에 누가 있는지(혹은 비었는지) 구현
near_seat = [[[0] * 4 for _ in range(n)] for _ in range(n)]

for x in range(n):
    for y in range(n):
        if x == 0 or x == n-1:
            near_seat[x][y].remove(0)
        if y == 0 or y == n-1:
            near_seat[x][y].remove(0)

# print(near_seat)

student_list = []

for _ in range(n**2):
    student_list.append(list(map(int, sys.stdin.readline().split())))

# 위 아래 왼쪽 오른쪽
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for student in student_list:
    student_num = student[0]
    prefer_list = student[1:]
    max_score = 0
    fin_x, fin_y = -1, -1

    personal_rank = []

    for x in range(n):
        for y in range(n):
            if seat_list[x][y] == 0:
                prefer_num = 0
                for i in prefer_list:
                    prefer_num += near_seat[x][y].count(i)
                personal_rank.append([prefer_num, near_seat[x][y].count(0), x, y])

    #print("before", personal_rank)
    personal_rank.sort(reverse=True)
    #print("after", personal_rank)

    fin_x = personal_rank[0][2]
    fin_y = personal_rank[0][3]

    seat_list[fin_x][fin_y] = student_num

    for i in range(4):
        nx = fin_x + dx[i]
        ny = fin_y + dy[i]
        if nx >= 0 and nx < n and ny >= 0 and ny < n and near_seat[nx][ny].count(0) > 0:
            near_seat[nx][ny].remove(0)
            near_seat[nx][ny].append(student_num)

result = 0

# print(seat_list)

for student in student_list:
    student_num = student[0]
    prefer_list = student[1:]
    cnt = 0
    for x in range(n):
        for y in range(n):
            if seat_list[x][y] == student_num:
                for i in prefer_list:
                    if near_seat[x][y].count(i) > 0:
                        cnt += 1
                if cnt == 1:
                    result += 1
                elif cnt == 2:
                    result += 10
                elif cnt == 3:
                    result += 100
                elif cnt == 4:
                    result += 1000
        if cnt > 0:
            break

print(result)
