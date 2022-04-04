import sys
import math
from itertools import combinations

map_arr = []
n, m = map(int, sys.stdin.readline().split(' '))
for _ in range(n):
    map_arr.append(list(sys.stdin.readline().rstrip().split(' ')))

chicken_arr = []
home_arr = []

for x in range(n):
    for y in range(n):
        if map_arr[x][y] == '2':
            chicken_arr.append((x, y))
        elif map_arr[x][y] == '1':
            home_arr.append((x, y))

home_count = len(home_arr)
chicken_count = len(chicken_arr)

chicken_list = [i for i in range(chicken_count)]

chicken_comb = list(combinations(chicken_list, m))

min_city_chicken_distance = 99999999
chicken_distance = [[0] * chicken_count for _ in range(home_count)]

for x in range(home_count):
    for y in range(chicken_count):
        x1, y1 = home_arr[x]
        x2, y2 = chicken_arr[y]
        chicken_distance[x][y] = int(math.fabs(x1-x2) + math.fabs(y1-y2))

for comb in chicken_comb:
    city_chicken_distance = 0
    for x in range(home_count):
        tmp_min = 9999
        for chicken_idx in comb:
            if chicken_distance[x][chicken_idx] < tmp_min:
                tmp_min = chicken_distance[x][chicken_idx]
        city_chicken_distance += tmp_min
    if city_chicken_distance < min_city_chicken_distance:
        min_city_chicken_distance = city_chicken_distance

print(min_city_chicken_distance)
