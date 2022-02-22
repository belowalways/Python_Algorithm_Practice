n = int(input())
cnt = 0


def sol_num(n):
    global cnt

    if n < 0:
        return

    sol_num(n-1)
    sol_num(n-2)
    sol_num(n-3)

    if n == 0:
        cnt += 1


case = []
for _ in range(n):
    case.append(int(input()))

for i in range(n):
    cnt = 0
    sol_num(case[i])
    print(cnt)

