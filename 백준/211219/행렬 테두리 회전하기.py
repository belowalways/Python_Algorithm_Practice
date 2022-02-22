n = int(input())
seq_list = map(int, input().split())
dp = []

max_idx = -1
max_len = 1

for seq in seq_list:
    dp.append([seq])

for i in range(n):
    for j in range(i):
        if seq_list[j] < seq_list[i]:
            if len(dp[j]) + 1 > len(dp[i]):
                dp[i] = dp[j] + [seq_list[j]]


for j in seq_list:
    if len(seq_list[j]) > max_len:
        max_len, max_idx = len(seq_list[j]), j

print(max_len)
print(*seq_list[max_idx])
