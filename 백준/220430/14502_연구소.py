from collections import deque
from copy import deepcopy

n, m = map(int, input().split())
lab_arr = []
for _ in range(n):
    lab_arr.append(list(map(int, input().split())))

virus = deque([])
lab_queue = deque([(lab_arr, 3)])
max_safe_zone = -1

for i in range(n):
    for j in range(m):
        if lab_arr[i][j] == 2:
            virus.append((i, j))

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def find_safe_zone(lab_arr):
    copyed_virus = deepcopy(virus)
    while copyed_virus:
        v = copyed_virus.popleft()
        x, y = v
        for d in range(4):
            nx, ny = x + dx[d], y + dy[d]
            if 0<=nx<n and 0<=ny<m:
                if lab_arr[nx][ny] == 0:
                    lab_arr[nx][ny] = 2
                    copyed_virus.append((nx, ny))
    cnt = 0
    for l in lab_arr:
        cnt += l.count(0)
    return cnt


for i in range(n):
    for j in range(m):
        if lab_arr[i][j] == 0:
            next_lab_queue = deque([])
            while lab_queue:
                lab_q = lab_queue.popleft()
                lab_arr, cnt = lab_q[0], lab_q[1]
                next_lab_queue.append((lab_arr, cnt))
                next_lab_arr = deepcopy(lab_arr)
                next_lab_arr[i][j] = 1
                cnt -= 1
                if cnt == 0:
                    safe_zone = find_safe_zone(next_lab_arr)
                    if safe_zone > max_safe_zone:
                        max_safe_zone = safe_zone
                else:
                    next_lab_queue.append((next_lab_arr, cnt))
            lab_queue = next_lab_queue

print(max_safe_zone)