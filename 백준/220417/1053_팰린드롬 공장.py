pellindrome = input()

str_list = [pellindrome]
str_length = len(pellindrome)


for i in range(1, len(pellindrome)):
    for j in range(i):
        if pellindrome[i] != pellindrome[j]:
            tmp_str = pellindrome[:j] + pellindrome[i] + pellindrome[j + 1:i] + pellindrome[j] + pellindrome[i + 1:]
            str_list.append(tmp_str)


def recursive_count(x, y):
    if x > y:
        return 0
    if dp[x][y] != 0:
        return dp[x][y]
    if tmp_str[x] == tmp_str[y]:
        dp[x][y] = recursive_count(x+1, y-1)
    else:
        dp[x][y] = min(1 + recursive_count(x + 1, y), 1 + recursive_count(x, y - 1), 1 + recursive_count(x+1, y-1))
    return dp[x][y]

answer = []

for tmp_str in str_list:
    dp = [[0] * str_length for _ in range(str_length)]
    answer.append(recursive_count(0, str_length - 1))

answer[0] += -1
print(min(answer) + 1)
