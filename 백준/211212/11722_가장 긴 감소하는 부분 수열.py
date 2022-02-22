'''
n = int(input())
a_seq = list(map(int, input().split()))
piece_list = [[1, a_seq[0]]]
for j in range(1, n):
    for piece in piece_list:
        if piece[1] > a_seq[j]:
            if piece_list.count([piece[0] + 1, a_seq[j]]) == 0:
                piece_list.append([piece[0] + 1, a_seq[j]])
    if piece_list.count([1, a_seq[j]]) == 0:
        piece_list.append([1, a_seq[j]])
    print(piece_list)

print((max(piece_list))[0])
'''

n = int(input())
a_seq = [0] + list(map(int, input().split()))
dp = [0] * 1001

for i in range(1, n + 1):
    for j in range(i):
        if a_seq[j] > a_seq[i]:
            dp[i] = max(dp[j] + 1, dp[i])

print(max(dp) + 1)
