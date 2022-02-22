n = int(input())

stair = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1] # 자리수가 0일때

for _ in range(n-1):
    stair = [stair[1],
             stair[0] + stair[2],
             stair[1] + stair[3],
             stair[2] + stair[4],
             stair[3] + stair[5],
             stair[4] + stair[6],
             stair[5] + stair[7],
             stair[6] + stair[8],
             stair[7] + stair[9],
             stair[8]
             ]

print(sum(stair) % 1000000000)
