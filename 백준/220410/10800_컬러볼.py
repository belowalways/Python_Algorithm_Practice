#https://www.acmicpc.net/problem/17143
from collections import defaultdict
import sys

n = int(sys.stdin.readline().rstrip())
balls = [list(map(int, sys.stdin.readline().rstrip().split())) + [i] for i in range(n)] #색깔, 크기, 순서
balls.sort(key=lambda x:x[1])

answer = defaultdict(int)
ball_size_sum = defaultdict(int)

total = 0
j = 0
for i in range(n):
    while balls[j][1] < balls[i][1] and j < n:
        total += balls[j][1]
        ball_size_sum[balls[j][0]] += balls[j][1]
        j += 1
    answer[balls[i][2]] = total - ball_size_sum[balls[i][0]]

for i in range(n):
    print(answer[i])
