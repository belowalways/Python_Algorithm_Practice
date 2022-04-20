max_ans = -10 ** 10
min_ans = 10 ** 10
ans_arr = []


def divide(a, b):
    if a < 0:
        return -((-a) // b)
    else:
        return a // b


def calculate(ans, i, plus, minus, mul, div, op_str):
    global max_ans
    global min_ans
    if i == n:
        if max_ans < ans:
            max_ans = ans
        if min_ans > ans:
            min_ans = ans
        return
    if plus > 0:
        calculate(ans + a_arr[i], i + 1, plus - 1, minus, mul, div, op_str + '+')
    if minus > 0:
        calculate(ans - a_arr[i], i + 1, plus, minus - 1, mul, div, op_str + '-')
    if mul > 0:
        calculate(ans * a_arr[i], i + 1, plus, minus, mul - 1, div, op_str + '*')
    if div > 0:
        calculate(divide(ans, a_arr[i]), i + 1, plus, minus, mul, div - 1, op_str + '/')


n = int(input())
a_arr = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())
calculate(a_arr[0], 1, plus, minus, mul, div, "")

print(max_ans)
print(min_ans)
