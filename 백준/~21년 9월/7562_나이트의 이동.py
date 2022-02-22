from collections import deque

n = int(input())
answer = []


def bfs(queue, visited):
    while queue:
        temp = queue.popleft()
        x = temp[0]
        y = temp[1]

        if visited[x][y] == 1:
            continue
        else:
            visited[x][y] = 1

        cnt = temp[2]

        if x == goal[0] and y == goal[1]:
            answer.append(cnt)
            queue.clear()
            break

        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < size and ny >= 0 and ny < size:
                    queue.append([nx, ny, cnt + 1])


for _ in range(n):
    size = int(input())
    start = list(map(int, input().split()))
    start.append(0)
    goal = list(map(int, input().split()))
    visited = [size * [0] for _ in range(size)]

    dx = [1, 1, -1, -1, 2, 2, -2, -2]
    dy = [2, -2, 2, -2, 1, -1, 1, -1]

    queue = deque([start])
    bfs(queue, visited)

for i in range(n):
    print(answer[i])