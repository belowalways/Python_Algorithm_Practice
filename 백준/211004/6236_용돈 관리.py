import sys

n, m = map(int, sys.stdin.readline().split())

cash_list = []

for _ in range(n):
    cash_list.append(int(sys.stdin.readline().strip()))

sum_cash = 0
for cash in cash_list:
    sum_cash += cash

min_cash = max(cash_list)
max_cash = sum_cash

while min_cash <= max_cash:
    mid_cash = (min_cash + max_cash) // 2
    # print("mid_cash", min_cash, mid_cash, max_cash)
    cnt = 0
    now_cash = 0

    for cash in cash_list:
        if now_cash < cash:
            now_cash = mid_cash
            cnt += 1
        now_cash -= cash
    # print("cnt", cnt)
    if cnt > m:
        min_cash = mid_cash + 1
    else:
        result = mid_cash
        max_cash = mid_cash - 1

print(result)

