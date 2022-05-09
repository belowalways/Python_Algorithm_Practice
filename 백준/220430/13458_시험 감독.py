n = int(input())
a_arr = list(map(int, input().split()))
b, c = map(int, input().split())
count = n
for i in range(n):
    a_arr[i] -= b
    if a_arr[i] > 0:
        count += a_arr[i] // c
        if a_arr[i] % c > 0:
            count += 1
print(count)
