n = int(input())
colorpaper_list = []

for _ in range(n):
    colorpaper_list.append(list(map(int, input().split())))

white_paper = 0
blue_paper = 0


def reculsive_colorpaper(x, y, n):
    global white_paper
    global blue_paper

    if colorpaper_list[x][y] == 0:
        for i in range(n):
            for j in range(n):
                if colorpaper_list[x + i][y + j] != 0:
                    reculsive_colorpaper(x, y, n // 2)
                    reculsive_colorpaper(x + n // 2, y, n // 2)
                    reculsive_colorpaper(x, y + n//2, n//2)
                    reculsive_colorpaper(x + n//2, y + n //2, n//2)
                    return
        white_paper = white_paper + 1

    if colorpaper_list[x][y] == 1:
        for i in range(n):
            for j in range(n):
                if colorpaper_list[x + i][y + j] != 1:
                    reculsive_colorpaper(x, y, n // 2)
                    reculsive_colorpaper(x + n // 2, y, n // 2)
                    reculsive_colorpaper(x, y + n//2, n//2)
                    reculsive_colorpaper(x + n//2, y + n //2, n//2)
                    return
        blue_paper = blue_paper + 1


reculsive_colorpaper(0, 0, n)

print(white_paper)
print(blue_paper)
