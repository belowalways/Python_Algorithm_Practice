n = int(input())
s_arr = [[]]
for _ in range(n):
    s_arr.append([0] + list(map(int, input().split())))

start_team = {1}
link_team = set()
origin_set = {i for i in range(1, n + 1)}

start_team_list = []
link_team_list = []

half_n = n // 2


def team_make(start_team, link_team, i):
    if len(start_team) == half_n:
        start_team_list.append(start_team)
        link_team_list.append(origin_set - start_team)
        return
    elif len(link_team) == half_n:
        start_team_list.append(origin_set - link_team)
        link_team_list.append(link_team)
        return
    team_make(start_team | {i}, link_team, i + 1)
    team_make(start_team, link_team | {i}, i + 1)


team_make(start_team, link_team, 2)
gap = 10 ** 6

for i in range(len(start_team_list)):
    i_start = list(start_team_list[i])
    i_link = list(link_team_list[i])
    start_team_score = 0
    link_team_score = 0
    for x in range(half_n):
        for y in range(half_n):
            start_team_score += s_arr[i_start[x]][i_start[y]]
            link_team_score += s_arr[i_link[x]][i_link[y]]
    i_gap = start_team_score - link_team_score
    if i_gap < 0:
        i_gap = -i_gap
    if i_gap < gap:
        gap = i_gap

print(gap)
