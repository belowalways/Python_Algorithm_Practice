from collections import deque

n, k = map(int, input().split())
line = []

line.append(input())
line.append(input())

# x, i, guard = 0, 1, 0
flag = False

queue = deque([[0, 0, 0]])

def jump(line, queue):
    global flag
    while queue:
        x, i, guard = map(int, queue.popleft())

        if i >= n:
            flag = True
            break
        if i < guard or line[x][i] == '0':
            continue

        line[0] = line[0][:guard] + '1' + line[0][guard + 1:]

        queue.append([x, i - 1, guard + 1])
        queue.append([x, i + 1, guard + 1])
        if x == 1:
            queue.append([0, i + k, guard + 1])
        else:
            queue.append([1, i + k, guard + 1])


jump(line, queue)
if flag:
    print(1)
else:
    print(0)
