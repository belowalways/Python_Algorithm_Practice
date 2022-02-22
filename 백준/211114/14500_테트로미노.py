n, m = map(int, input().split())
paper = []
for _ in range(n):
    paper.append(list(map(int, input().split())))

max_sum = 0

# 위 오른쪽 아래 왼쪽
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

move_list = [[1,1,1],[2,2,2],[1,2,3],[2,1,2],[0,1,0],[1,0,1],[3,0,3],[2,2,1],[2,2,3],[1,2,2],[3,2,2],[1,1,0],[1,1,2],[2,1,1],[0,1,1]]
move_list_2 = [[1,1,2,3],[1,1,0,3],[2,2,3,0],[2,2,1,0]]


def move_1(move_list):
    global max_sum
    for i in range(n):
        for j in range(m):
            for move in move_list:
                x, y = i, j
                tmp_sum = paper[x][y]
                for k in move:
                    nx, ny = x + dx[k], y + dy[k]
                    if 0<=nx<n and 0<=ny<m:
                        tmp_sum += paper[nx][ny]
                        x, y = nx, ny
                    else:
                        #print(i, j, move, nx, ny)
                        tmp_sum = 0
                        break
                #print(i, j, move, tmp_sum)
                if tmp_sum > max_sum:
                    max_sum = tmp_sum


def move_2(move_list):
    global max_sum
    for i in range(n):
        for j in range(m):
            for move in move_list:
                x, y = i, j
                tmp_sum = paper[x][y]
                for o in range(len(move)):
                    k = move[o]
                    nx, ny = x + dx[k], y + dy[k]
                    if 0<=nx<n and 0<=ny<m:
                        x, y = nx, ny
                        if o != 2:
                            tmp_sum += paper[nx][ny]
                    else:
                        break
                if tmp_sum > max_sum:
                    max_sum = tmp_sum
                else:
                    continue


move_1(move_list)
move_2(move_list_2)
print(max_sum)
