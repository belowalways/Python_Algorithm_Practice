from collections import deque
n, m = map(int, input().split())
queue = deque([[n, m]])
split = 0

while queue:
    x, y = map(int, queue.popleft())

    if x == 1 and y == 1:
        continue

    if x > y:
        queue.append([int(x/2), y])
        queue.append([x - int(x/2), y])
    else:
        queue.append([x, int(y/2)])
        queue.append([x, y - int(y/2)])
    split += 1

print(split)
