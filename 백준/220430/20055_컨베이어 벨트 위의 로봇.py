from collections import deque
n, k = map(int, input().split())
robot_arr = [0] * (2 * n)
belt_arr = list(map(int, input().split()))
belt_queue = deque(belt_arr)

step = 0

while True:
    step += 1
    belt_arr = [belt_arr[-1]] + belt_arr[:-1]
    robot_arr = [robot_arr[-1]] + robot_arr[:-1]
    robot_arr[n-1] = 0
    for i in range(n - 2, -1, -1):
        if robot_arr[i] == 1 and robot_arr[i + 1] == 0 and belt_arr[i + 1] >= 1:
            robot_arr[i] = 0
            robot_arr[i + 1] = 1
            belt_arr[i + 1] -= 1
    robot_arr[n - 1] = 0
    if belt_arr[0] != 0:
        robot_arr[0] = 1
        belt_arr[0] -= 1
    if belt_arr.count(0) >= k:
        break

print(step)


