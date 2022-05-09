n, l = map(int, input().split())
load = [list(map(int, input().split())) for _ in range(n)]


dp = [[0] * n for _ in range(n)]

fine_row = 0
for x in range(n):
    dp[x][0] = 1
    for y in range(1, n):
        if load[x][y] == load[x][y-1]:
            dp[x][y] = dp[x][y-1] + 1
        elif load[x][y] == load[x][y-1] + 1:
            if dp[x][y-1] >= l:
                dp[x][y] = 1
            else:
                break
        elif load[x][y] + 1 == load[x][y-1]:
            if dp[x][y-1] < 0:
                break
            dp[x][y] = -l+1
        else:
            break
    else:
        if dp[x][-1] >= 0:
            # print(x, dp[x])
            fine_row += 1

# print(fine_row)

dp = [[0] * n for _ in range(n)]
fine_column = 0
for y in range(n):
    dp[0][y] = 1
    for x in range(1, n):
        if load[x][y] == load[x-1][y]:
            dp[x][y] = dp[x-1][y] + 1
        elif load[x][y] == load[x-1][y] + 1:
            if dp[x-1][y] >= l:
                dp[x][y] = 1
            else:
                break
        elif load[x][y] + 1 == load[x-1][y]:
            if dp[x-1][y] < 0:
                break
            dp[x][y] = -l+1
        else:
            break
    else:
        if dp[-1][y] >= 0:
            '''print(y, end=' ')
            for i in range(n):
                print(dp[i][y], end=' ')
            print()'''
            fine_column += 1

# print(fine_column)
print(fine_row + fine_column)

'''fill = [[0] * n for _ in range(n)]
fine_load = 0
for x in range(n):
    tmp = load[x][0]
    count = 1
    escape = False
    y = 1
    for y in range(1, n):
        if tmp == load[x][y]:
            count += 1
        else:
            if load[x][y] == load[x][y-1] + 1 and count >= l:
                for j in range(y-l, y):
                    if not fill[x][j]:
                        fill[x][j] = 1
                    else:
                        escape = True
                        break
                else:
                    tmp = load[x][y]
                    count = 1
            elif load[x][y] + 1 == load[x][y-1]:
                
            else:
                break
        if escape:
            break
    else:
        fine_load += 1


fill = [[0] * n for _ in range(n)]
for y in range(n):
    for x in range(n):'''