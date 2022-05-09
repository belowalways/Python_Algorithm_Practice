from collections import deque

n, m, t = map(int, input().split())
circle_list = [deque([])]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
answer = 0


for _ in range(n):
    queue = deque(list(map(int, input().split())))
    circle_list.append(queue)

for _ in range(t):
    '''print("circles:")
    for circle in circle_list:
        print(circle)'''

    x, d, k = map(int, input().split())
    now_circle_sum = 0
    for i in range(1, n + 1):
        now_circle_sum += sum(circle_list[i])
        if i % x == 0:
            if d == 0:
                circle_list[i].rotate(k % m)
            else:
                circle_list[i].rotate(-k % m)

    '''print("circles:")
    for circle in circle_list:
        print(circle)'''
    if now_circle_sum == 0:
        break

    remove_set = set()

    for x in range(1, n + 1):
        for y in range(m):
            if circle_list[x][y] != 0:
                for d in range(4):
                    nx, ny = x + dx[d], y + dy[d]
                    if ny == m:
                        ny = 0
                    if ny == -1:
                        ny = m - 1
                    if 0<nx<=n and circle_list[nx][ny] == circle_list[x][y]:
                        remove_set.add((x, y))
                        remove_set.add((nx, ny))

    if len(remove_set) == 0:
        removed_count = 0
        now_circle_sum = 0
        for circle in circle_list:
            removed_count += circle.count(0)
            now_circle_sum += sum(circle)
        if n * m - removed_count != 0:
            avg = now_circle_sum / float(n * m - removed_count)
            for x in range(1, n + 1):
                for y in range(m):
                    if circle_list[x][y] != 0:
                        if circle_list[x][y] > avg:
                            circle_list[x][y] -= 1
                        elif circle_list[x][y] < avg:
                            circle_list[x][y] += 1
    else:
        for (i, j) in remove_set:
            circle_list[i][j] = 0


#print("final_circle")
for circle in circle_list:
    #print(circle)
    answer += sum(circle)

print(answer)







