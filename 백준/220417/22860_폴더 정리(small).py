from collections import defaultdict
import sys
sys.setrecursionlimit(10 ** 6)
n, m = map(int, input().split())
folder = [set() for _ in range(n + 1)]
file_list = [defaultdict(int) for _ in range(n + 1)]

folder_idx_dict = {"main": 0}
tmp = 1
for _ in range(n + m):
    upper_folder, lower, file_or_folder = input().split()
    if upper_folder not in folder_idx_dict.keys():
        folder_idx_dict[upper_folder] = tmp
        tmp += 1
    # folder
    if file_or_folder == '0':
        file_list[folder_idx_dict[upper_folder]][lower] += 1
    else:
        if lower not in folder_idx_dict.keys():
            folder_idx_dict[lower] = tmp
            tmp += 1
        folder[folder_idx_dict[upper_folder]].add(folder_idx_dict[lower])

q = int(input())

#print(folder_idx_dict)
#print(file_list)


def file_count(idx):
    global tmp_dict
    for key in file_list[idx]:
        tmp_dict[key] += file_list[idx][key]
    for f in folder[idx]:
        file_count(f)

for _ in range(q):
    tmp_list = list(input().split('/'))
    tmp_dict = defaultdict(int)
    start_idx = folder_idx_dict[tmp_list[-1]]
    file_count(start_idx)
    file_type_count, file_total_count = len(tmp_dict), sum(tmp_dict.values())
    print(file_type_count, file_total_count)




