from collections import deque

n, k = list(map(int, input().split()))
kit_list = list(map(int, input().split()))
for i in range(n):
    kit_list[i] -= k

weight = 0
cnt = 0

queue = deque([[weight, kit_list]])

while queue:
    weight, kit_list = queue.popleft()

    if len(kit_list) > 0:
        for i in range(len(kit_list)):
            if weight + kit_list[i] >= 0:
                tmp_list = kit_list[:]
                tmp_list.remove(kit_list[i])
                queue.append([weight + kit_list[i], tmp_list])
    else:
        cnt += 1

print(cnt)
