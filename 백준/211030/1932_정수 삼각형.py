n = int(input())

triangle = []
for _ in range(n):
    triangle.append(list(map(int, input().split(' '))))

for i in range(1, n):
    for j in range(n-i):
        if triangle[n-i][j] < triangle[n-i][j+1]:
            triangle[n-i-1][j] += triangle[n-i][j+1]
        else:
            triangle[n-i-1][j] += triangle[n-i][j]
        # print(triangle)

print(triangle[0][0])
