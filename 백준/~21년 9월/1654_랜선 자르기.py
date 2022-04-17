# 1654번 랜선 자르기

import math
import sys

k, n = 2, 4

k_list = []
k_under = []
k_per = []
k_sum = 0

for _ in range(k):
    k_list.append(int(sys.stdin.readline().rstrip()))

for i in k_list:
    k_sum = k_sum + i

for j in k_list:
    k_per.append(j * n / k_sum) # 필요한 랜선 몇 개가 배정되어야 하는지
    k_under.append((j * n / k_sum) - (j * n // k_sum)) # 소숫점 아래

minValue = min(k_under)
minIdx = -1
for u in range(len(k_under)):
    if k_under[u] == minValue:
        minIdx = u
        break

# 소숫점 아래가 가장 작은 거 기준 올림해서 몫을 front로 함
front = k_list[minIdx] // math.ceil(k_per[minIdx])
back = k_sum // n

# print(front, back)
# while front != back and (front + 1) != back:
while front != back and (front + 1) != back:
    # print(front, back)
    mid = int((front + back) / 2)
    # print(mid)
    tmp_list = []
    for m in k_list:
        tmp_list.append(m // mid)
    # print(tmp_list)
    if sum(tmp_list) >= n:
        front = mid
    else:
        back = mid - 1

temp_list = []

for w in k_list:
    temp_list.append(w // back)

if sum(temp_list) >= n:
    print(back)
else:
    print(front)
