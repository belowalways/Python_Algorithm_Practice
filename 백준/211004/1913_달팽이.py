# 1913_달팽이.py
# 홀수인 자연수 N이 주어지면, 다음과 같이 1부터 N^2까지의 자연수를 달팽이 모양으로 N×N의 표에 채울 수 있다.
# 런타임 에러 (UnboundLocalError) -> 1이 target일 경우를 생각 못했기 때문

n = int(input())
t = int(input())

if n == 1:
    snail_list = [[1]]
else:
    snail_list = [[0] * n for _ in range(n)]

# 위, 오른쪽, 아래, 왼쪽 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def fill_snail(snail_list, t):
    if n == 1:
        snail_list[0][0] = 1
        tar_x, tar_y = 1, 1
    else:
        m = 1
        x = n//2
        y = n//2
        tar_x, tar_y = x + 1, y + 1
        snail_list[x][y] = m
        i = 2
        while i < n:
            move_list = [0] + [1] * (i-1) + [2] * i + [3] * i + [0] * i
            for j in move_list:
                m += 1
                x = x + dx[j]
                y = y + dy[j]
                snail_list[x][y] = m
                if m == t:
                    tar_x, tar_y = x + 1, y + 1
            i += 2

    return snail_list, tar_x, tar_y


snail_list, tar_x, tar_y = fill_snail(snail_list, t)

for k in snail_list:
    print(*k)

print(tar_x, tar_y)

