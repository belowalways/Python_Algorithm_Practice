n = int(input())

sequence = list(map(int, input().split()))

stack = []
NGE = [-1 for _ in range(n)]

stack.append(0)
i = 1

while i < n:
    while stack and sequence[stack[-1]] < sequence[i]:
        NGE[stack[-1]] = sequence[i]
        stack.pop()

    stack.append(i)
    i += 1

print(*NGE)
