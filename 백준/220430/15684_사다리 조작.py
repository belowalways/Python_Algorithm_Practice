n, m, h = map(int, input().split())

ladder = [[0] * (n-1) for _ in range(h)]
for _ in range(m):
    a, b = map(int, input().split())
    ladder[a-1][b-1] = 1


def check_answer(ladder):
    result = False
    ladder_answer = [i for i in range(n)]
    for x in range(h):
        for y in range(n - 1):
            if ladder[x][y] != 0:
                tmp = ladder_answer[y]
                ladder_answer[y] = ladder_answer[y - 1]
                ladder_answer[y - 1] = tmp
    for i in range(n):
        if ladder_answer[i] != i:
            break
    else:
        result = True
    return result



if check_answer(ladder):
    print(0)
else:
    empty_ladder = []
    for x in range(h):
        for y in range(n - 1):
            if ladder[x][y] == 0:
                empty_ladder.append((x, y))
    empty_length = len(empty_ladder)
    answer = -1

    def dfs(count, idx, ladder):
        global answer
        x, y = empty_ladder[idx]

        if y > 0 and ladder[x][y-1] == 1 or y + 1 < n - 1 and ladder[x][y+1] == 1:
            return

        ladder[x][y] = 1
        if check_answer(ladder):
            if answer == -1:
                answer = count
            else:
                answer = min(count, answer)
        else:
            if count <= 2 and idx + 1 < empty_length:
                for i in range(idx + 1, empty_length):
                    dfs(count + 1, i, [row[:] for row in ladder])

    for j in range(empty_length):
        dfs(1, j, [row[:] for row in ladder])

    print(answer)








'''n, m, h = map(int, input().split())

ladder_arr = [[0] * n for _ in range(h)]

for _ in range(m):
    a, b = map(int, input().split())
    ladder_arr[a-1][b-1] = 1

# find empty ladder
empty_ladder_list = []

for i in range(h):
    for j in range(n - 1):
        if ladder_arr[i][j] == 0:
            if j > 0:
                if ladder_arr[i][j-1] != 0:
                    continue
            if j < n - 2:
                if ladder_arr[i][j+1] != 0:
                    continue
            empty_ladder_list.append((i, j))


def check_answer(ladder_arr):
    ans_arr = [i for i in range(n)]
    for i in range(h):
        for j in range(n - 1):
            if ladder_arr[i][j] == 1:
                tmp = ans_arr[j]
                ans_arr[j] = ans_arr[j + 1]
                ans_arr[j + 1] = tmp
    for i in range(n):
        if ans_arr[i] != i:
            return False
    return True


def make_comb_ladder(empty_ladder_list, n):
    len_arr = len(empty_ladder_list)
    result = []

    def dfs(start, visited):
        if len(visited) == n:
            result.append(visited[:])
            return

        for idx in range(start, len_arr):
            if len(visited) > 1:
                if visited[-1][0] == empty_ladder_list[idx][0] and empty_ladder_list[idx][0] - visited[-1][0] == 1:
                    continue
            visited.append(empty_ladder_list[idx])
            dfs(idx + 1, visited)
            visited.pop()

    dfs(0, [])
    return result


if check_answer(ladder_arr):
    print(0)
else:
    for i in range(1, 4):
        comb_ladder = make_comb_ladder(empty_ladder_list, i)
        for comb in comb_ladder:
            tmp_ladder_arr = [a[:] for a in ladder_arr]
            for (x, y) in comb:
                tmp_ladder_arr[x][y] = 1
            if check_answer(tmp_ladder_arr):
                print(i)
                exit(0)
    print(-1)
'''