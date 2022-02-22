dp = []

dp.append(1)
dp.append(1)
dp.append(3)
for i in range(3, 251):
    num = dp[i - 1] + 2 * dp[i - 2]
    dp.append(num)

while 1:
    try:
        x = int(input())
        print(dp[x])
    except:
        break