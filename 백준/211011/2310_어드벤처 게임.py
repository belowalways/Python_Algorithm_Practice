import sys
sys.setrecursionlimit(10 ** 6)

answer = []

def dfs_maze_explore(maze_list, visited, p, money):
    global escape

    # print("p, money = ", p, money)

    if maze_list[p][0] == 'L':
        if money < maze_list[p][1]:
            money = maze_list[p][1]
    elif maze_list[p][0] == 'T':
        if money >= maze_list[p][1]:
            money -= maze_list[p][1]
        else:
            return

    if len(maze_list) - 1 == p:
        escape = True
        return

    for room in maze_list[p][2:]:
        if p != room and not visited[room]:
            visited[room] = True
            dfs_maze_explore(maze_list, visited, room, money)
            visited[room] = False
    visited[p] = False

while True:
    n = int(sys.stdin.readline())

    if n == 0:
        for ans in answer:
            if ans:
                print("Yes")
            else:
                print("No")
        break

    maze_list = [[]]
    in_room_list = []
    escape = False
    visited = [0] * (n + 1)
    for _ in range(n):
        tmp = sys.stdin.readline().split()
        in_room = tmp[0]
        door_list = list(map(int, tmp[1:-1]))
        maze_list.append([in_room] + door_list)

    dfs_maze_explore(maze_list, visited, 1, 0)
    answer.append(escape)
