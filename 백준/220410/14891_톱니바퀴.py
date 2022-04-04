def spin(cycle_num, direction):
    global state
    global visited
    visited[cycle_num] = True

    #print(cycle_num, direction)

    if cycle_num - 1 > 0:
        if not visited[cycle_num - 1] and state[cycle_num][6] != state[cycle_num-1][2]:
            spin(cycle_num-1, -direction)
    if cycle_num + 1 <= 4:
        if not visited[cycle_num + 1] and state[cycle_num + 1][6] != state[cycle_num][2]:
            spin(cycle_num+1, -direction)

    if direction == 1:
        state[cycle_num] = state[cycle_num][-1] + state[cycle_num][:-1]
    else:
        state[cycle_num] = state[cycle_num][1:] + state[cycle_num][0]


state = [[]]

for _ in range(4):
    state.append(input())

cycle = []
k = int(input())

visited = []

for _ in range(k):
    visited = [True] + [False] * 4
    cycle_num, direction = map(int, input().split(' '))
    #print("start")
    spin(cycle_num, direction)

#print(state)

print(int(state[1][0]) * 1 + int(state[2][0]) * 2 + int(state[3][0]) * 4 + int(state[4][0]) * 8)

