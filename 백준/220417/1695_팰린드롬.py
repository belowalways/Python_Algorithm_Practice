import sys
input = sys.stdin.readline

n = int(input())
num_list = list(map(int, input.split()))

dp = [[0] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if num_list[-i] == num_list[j - 1]: # 뒤집은 수열 i-1번째와 그냥 수열의 j-1번째가 같으면
            dp[i][j] = dp[i-1][j-1] + 1
        else: # 다르면
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

print(n - dp[-1][-1])
