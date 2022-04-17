from copy import deepcopy
from itertools import permutations
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())

office_arr = []
cctv_idx_arr = []

for x in range(n):
    temp = list(map(int, sys.stdin.readline().rstrip().split()))
    for y in range(m):
        if 1 <= temp[y] <= 5:
            cctv_idx_arr.append((x, y, temp[y]))
    office_arr.append(temp)

# 위 오른쪽 아래 왼쪽
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

'''
1번 -> 4
[(0), (1), (2), (3)]
2번 -> 2
[(1, 3), (0, 2)]
3번 -> 4
[(0, 1), (1, 2), (2, 3), (3, 4)]
4번 -> 4
[(0, 1, 2), (1, 2, 3), (2, 3, 0), (3, 0, 1)]
5번 -> 1
[(0, 1, 2, 3)]
'''

cctv_list = [
    [],
    [(0,), (1,), (2,), (3,)],
    [(1, 3), (0, 2)],
    [(0, 1), (1, 2), (2, 3), (3, 0)],
    [(0, 1, 2), (1, 2, 3), (2, 3, 0), (3, 0, 1)],
    [(0, 1, 2, 3)]
]

answer = 10000


def dfs(office_arr, idx):
    global answer

    if idx == len(cctv_idx_arr):
        tmp_answer = 0
        for o in office_arr:
            tmp_answer += o.count(0)
        if tmp_answer < answer:
            answer = tmp_answer
        return

    x, y, cctv_type = cctv_idx_arr[idx]
    for dir_list in cctv_list[cctv_type]:
        tmp_office_arr = deepcopy(office_arr)
        for d in dir_list:
            nx, ny = x, y
            while True:
                nx += dx[d]
                ny += dy[d]
                if 0 <= nx < n and 0 <= ny < m:
                    if tmp_office_arr[nx][ny] == 6:
                        break
                    elif tmp_office_arr[nx][ny] == 0:
                        tmp_office_arr[nx][ny] = -1
                else:
                    break
        dfs(tmp_office_arr, idx + 1)


dfs(office_arr, 0)
print(answer)
