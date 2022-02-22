n = int(input())
sequence = []

for m in range(n):
    sequence.append(int(input()))

max_num = 0

stack = []
for_print = []

for i in sequence:
    if i > max_num:
        for j in range(i - max_num):
            stack.append(max_num + j + 1)
            #print(stack)
            for_print.append('+')
        stack.pop()
        for_print.append('-')
        max_num = i
    elif stack[-1] == i:
        for_print.append('-')
        stack.pop()
    else:
        print('NO')
        for_print = []
        break
    #print(for_print)
    #print(stack)

for k in for_print:
    print(k)

