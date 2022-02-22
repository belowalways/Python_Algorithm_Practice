x = int(input())
dp = [0, 0, 1, 1] + [0] * (10**6)

for n in range(4, x + 1):
    dp[n] = dp[n-1] + 1
    if n % 2 == 0:
        dp[n] = min(dp[n], dp[n//2] + 1)
    if n % 3 == 0:
        dp[n] = min(dp[n], dp[n//3] + 1)

print(dp[x])
