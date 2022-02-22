# 14720번 우유 축제

n = int(input())
shop_list = list(map(int, input().split()))

want = 0
cnt = 0

for i in shop_list:
    if i == want:
        cnt += 1
        want += 1
        if want == 3:
            want = 0

print(cnt)
