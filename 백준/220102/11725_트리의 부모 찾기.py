n = int(input())

node_list = [[] for _ in range (n + 1)]
parent_list = [0] * (n + 1)

for _ in range(n-1):
    x, y = map(int, input().split())
    node_list[x].append(y)
    node_list[y].append(x)

print(node_list)

while True:
    for node in node_list[1]:
        parent_list[node] = node_list[1]