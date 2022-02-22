n = int(input())

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(n):
    for j in range(n):
        while board[x + dx[k]][y + dy[k]] == 0:
            x += dx[k]
            y += dy[k]

# ?? dfs
