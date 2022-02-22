from collections import deque

s = int(input())
queue = deque([1, 0])
print(queue)


def bfs(s, clipBoard):
    now = []
    while queue:
        now = queue.popleft()

        # 1번 연산
        queue.append([now[0], now[0]])

        # 2번 연산
        queue.append([now[0] + now[1], now[1]])
