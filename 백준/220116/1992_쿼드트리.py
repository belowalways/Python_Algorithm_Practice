n = int(input())

video_list = []

for _ in range(n):
    video_list.append(input())

def recursive_zip(x, y, n):
    #print('x, y, n = ', x, y, n)

    if video_list[x][y] == '0':
        for i in range(n):
            for j in range(n):
                if video_list[x + i][y + j] != '0':
                    print('(', end='')
                    recursive_zip(x, y, n//2)
                    recursive_zip(x, y + n // 2, n // 2)
                    recursive_zip(x + n // 2, y, n // 2)
                    recursive_zip(x + n // 2, y + n // 2, n // 2)
                    print(')', end='')
                    return
        print('0', end='')
    elif video_list[x][y] == '1':
        for i in range(n):
            for j in range(n):
                if video_list[x + i][y + j] != '1':
                    print('(', end='')
                    recursive_zip(x, y, n // 2)
                    recursive_zip(x, y + n // 2, n // 2)
                    recursive_zip(x + n // 2, y, n // 2)
                    recursive_zip(x + n // 2, y + n // 2, n // 2)
                    print(')', end='')
                    return
        print('1', end='')


recursive_zip(0, 0, n)
