import sys
sys.setrecursionlimit(10**6)

n = int(input())

gameBoard = []
visited = [[0] * n for _ in range(n)]

for _ in range(n):
    temp = list(map(int, input().split()))
    gameBoard.append(temp)

cnt = 0


def dfs(x, y, visited):
    if x >= n or y >= n or visited[x][y] == 1:
        return

    visited[x][y] = 1

    if gameBoard[x][y] == -1:
        print("HaruHaru")
        return
    else:
        dfs(x + gameBoard[x][y], y, visited)
        dfs(x, y + gameBoard[x][y], visited)

    if visited[n-1][n-1] != 1 and x == 0 and y == 0:
        print("Hing")


dfs(0, 0, visited)
