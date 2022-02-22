n = int(input())
road_list = list(map(int, input().split()))
city_list = list(map(int, input().split()))

cash = road_list[0] * city_list[0]
oil = city_list[0]

for tmp in range(1, len(road_list)):
    if oil > city_list[tmp]:
        oil = city_list[tmp]
    cash += oil * road_list[tmp]

print(cash)
