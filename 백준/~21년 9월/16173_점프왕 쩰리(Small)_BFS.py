from collections import deque

n = int(input())

gameBoard = []
visited = [[0] * n for _ in range(n)]

for _ in range(n):
    temp = list(map(int, input().split()))
    gameBoard.append(temp)

queue = deque([[0, 0]])


def bfs(queue):
    while queue:
        v = queue.popleft()

        x = v[0]
        y = v[1]
        val = gameBoard[x][y]
        visited[x][y] = 1

        if val == -1:
            print("HaruHaru")
            break

        if x + val < n and visited[x + val][y] == 0:
            queue.append([x + val, y])
        if y + val < n and visited[x][y + val] == 0:
            queue.append([x, y + val])

    if visited[n-1][n-1] == 0:
        print("Hing")


bfs(queue)
