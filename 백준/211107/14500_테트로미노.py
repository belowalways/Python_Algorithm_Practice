from collections import deque

n, m = map(int, input().split())
paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))

max_sum = 0

# 위 오른쪽 아래 왼쪽
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

move_list_1 = [[2, 2, 1], [2, 1, 2], [2, 2, 3], [2, 3, 2]]
move_list_2 = [[1, 1, 3, 2]]


def make_move_list(move_list):
    custom_list = []
    for move in move_list:
        custom_list.append(move)
        for k in range(3):
            for i in range(len(move)):
                new_move = move[:]
                new_move[i] += k + 1
                if new_move[i] > 3:
                    new_move[i] %= 3
            custom_list.append(new_move)
            print(custom_list)
    return custom_list


full_move_list = [[1, 1, 1], [1, 2, 3], [2, 2, 2]] + make_move_list(move_list_1)
full_move_list_2 = make_move_list(move_list_2)

print(full_move_list)
print(full_move_list_2)





def move_2(move_list):
    global max_sum
    for i in range(n):
        for j in range(m):
            x, y = i, j
            for move in move_list:
                tmp_sum = paper[x][y]
                for m in len(move):
                    nx, ny = x + dx[k], y + dy[k]
                    if 0<=nx<n and 0<=ny<m:
                        tmp_sum += paper[nx][ny]
                        x, y = nx, ny
                    else:
                        break
                if tmp_sum > max_sum:
                    max_sum = tmp_sum
                else:
                    continue


move_1(full_move_list)
print(max_sum)
