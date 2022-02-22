n = int(input())

T = []
P = []

dp = [0] * (n + 1)

for _ in range(n):
    t, p = map(int, input().split())
    T.append(t)
    P.append(p)

i = 0

while i < n:
    tmp = i + T[i]
    if dp[i - 1] > dp[i]:
        dp[i] = dp[i - 1]
    if tmp < (n + 1) and dp[i] + P[i] >= dp[tmp]:
        dp[tmp] = dp[i] + P[i]
    i += 1

print(max(dp))
