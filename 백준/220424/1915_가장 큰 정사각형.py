n, m = map(int, input().split())
dp = [[0] * m for _ in range(n)]
q_arr = []

for _ in range(n):
    q_arr.append([int(i) for i in input()])

answer = -1

for i in range(n):
    for j in range(m):
        if q_arr[i][j] == 1:
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = min(dp[i][j-1], dp[i-1][j-1], dp[i-1][j]) + 1
    tmp_ans = max(dp[i])
    if tmp_ans > answer:
        answer = tmp_ans

print(answer * answer)