g = int(input())

num_list = [1]
plus_list = [1]
ans_list = []

while plus_list[-1] <= g:
    num_list.append(num_list[-1] + 1)
    plus_list.append(num_list[-1] ** 2 - num_list[-2] ** 2)

# print(plus_list)

for i in num_list:
    for n in range(len(plus_list)):
        a = plus_list[i - 1]
        s = (n*(2*a+(n-1)*2))/2 # 등차수열의 합
        if s > g:
            break
        if s == g:
            ans_list.append(i + (n - 1))
            break


if len(ans_list) == 0:
    print(-1)
else:
    for ans in ans_list:
        print(ans)
