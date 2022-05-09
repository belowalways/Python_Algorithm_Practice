import math
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]


def full_choice():
    answer = []
    for d1 in range(1, n - 1):
        for d2 in range(1, n - 1):
            for x in range(1, n + 1):
                for y in range(1, n + 1):
                    if 1<=x<x+d1+d2<=n and 1<=y-d1<y<y+d2<=n:
                        answer.append((x, y, d1, d2))

    return answer


choices = full_choice()

ans = math.inf

for choice in choices:
    people = [0] * 5
    x, y, d1, d2 = choice
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if x + y <= i + j <= x + y + d2 * 2 and x - y <= i - j <= x - y + 2 * d1:
                people[4] += arr[i-1][j-1]
            elif 1 <= i < x + d1 and 1 <= j <= y:
                people[0] += arr[i-1][j-1]
            elif 1 <= i <= x + d2 and y < j <= n:
                people[1] += arr[i-1][j-1]
            elif x + d1 <= i <= n and 1 <= j < y - d1 + d2:
                people[2] += arr[i-1][j-1]
            elif x + d2 < i <= n and y - d1 + d2 <= j <= n:
                people[3] += arr[i-1][j-1]
    gap = max(people) - min(people)
    if ans > gap:
        ans = gap

print(ans)
