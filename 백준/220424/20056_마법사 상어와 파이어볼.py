from collections import defaultdict

n, m, k = map(int, input().split())

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, 1, 1, 1, 0, -1, -1, -1]

shark_dict = defaultdict(list)


def move_shark(shark_dict):
    new_shark_dict = defaultdict(list)
    for key in shark_dict:
        for shark in shark_dict[key]:
            r, c = key
            m, s, d = shark[0], shark[1], shark[2]
            r += dx[d] * (s % n)
            c += dy[d] * (s % n)
            if r > 0:
                r %= n
            elif r < 0:
                r += n
            if c > 0:
                c %= n
            elif c < 0:
                c += n
            new_shark_dict[(r, c)] += [shark]
    return new_shark_dict


def divide_shark(shark_dict):
    new_shark_dict = defaultdict(list)
    for key in shark_dict:
        if len(shark_dict[key]) > 1:
            sum_of_m = 0
            sum_of_s = 0
            odd_or_even = [0, 0]

            for shark in shark_dict[key]:
                m, s, d = shark[0], shark[1], shark[2]
                sum_of_m += m
                sum_of_s += s
                odd_or_even[d % 2] += 1
            m = sum_of_m // 5

            if m == 0:
                continue

            s = sum_of_s // len(shark_dict[key])

            if odd_or_even[0] > 0 and odd_or_even[1] > 0:
                new_shark_dict[key] += [[m, s, 1]]
                new_shark_dict[key] += [[m, s, 3]]
                new_shark_dict[key] += [[m, s, 5]]
                new_shark_dict[key] += [[m, s, 7]]
            else:
                new_shark_dict[key] += [[m, s, 0]]
                new_shark_dict[key] += [[m, s, 2]]
                new_shark_dict[key] += [[m, s, 4]]
                new_shark_dict[key] += [[m, s, 6]]
        else:
            new_shark_dict[key] += shark_dict[key]
    return new_shark_dict


def count_shark(shark_dict):
    sum_of_m = 0
    for key in shark_dict:
        for shark in shark_dict[key]:
            sum_of_m += shark[0]
    return sum_of_m


for _ in range(m):
    r, c, m, s, d = map(int, input().split())
    shark_dict[(r-1, c-1)] += [[m, s, d]]

for _ in range(k):
    shark_dict = divide_shark(move_shark(shark_dict))

print(count_shark(shark_dict))