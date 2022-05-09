from collections import defaultdict

answer = -1
r, c, k = map(int, input().split())
r, c = r-1, c-1
a_arr = [[0] * 100 for _ in range(100)]
for i in range(3):
    x, y, z = map(int, input().split())
    a_arr[i][0] = x
    a_arr[i][1] = y
    a_arr[i][2] = z

is_big_row = True
row = 3
column = 3

'''print(row, column)
for a in a_arr:
    print(a)'''

if a_arr[r][c] == k:
    answer = 0
else:
    answer = -1
    for t in range(1, 101):
        new_a_arr = [[0] * 100 for _ in range(100)]
        if is_big_row:
            max_idx = 0
            for i in range(row):
                tmp_dict = defaultdict(int)
                for j in range(column):
                    tmp_dict[a_arr[i][j]] += 1
                idx = 0
                tmp_list = list(zip(tmp_dict.keys(), tmp_dict.values()))
                tmp_list.sort(key=lambda x: (x[1], x[0]))
                for (key, value) in tmp_list:
                    if key != 0 and idx < 100:
                        new_a_arr[i][idx] = key
                        new_a_arr[i][idx + 1] = value
                        idx += 2
                if max_idx < idx:
                    max_idx = idx
            column = max_idx
            if row < column:
                is_big_row = False
        else:
            max_idx = 0
            for j in range(column):
                tmp_dict = defaultdict(int)
                for i in range(row):
                    tmp_dict[a_arr[i][j]] += 1
                idx = 0
                tmp_list = list(zip(tmp_dict.keys(), tmp_dict.values()))
                tmp_list.sort(key=lambda x: (x[1], x[0]))
                for (key, value) in tmp_list:
                    if key != 0 and idx < 100:
                        new_a_arr[idx][j] = key
                        new_a_arr[idx + 1][j] = value
                        idx += 2
                if max_idx < idx:
                    max_idx = idx
            row = max_idx
            if row >= column:
                is_big_row = True
        a_arr = new_a_arr

        '''print(row, column)
        for a in a_arr:
            print(a)'''

        if a_arr[r][c] == k:
            answer = t
            break

print(answer)



'''if a_arr[r][c] == k:
    answer = 0
else:
    for t in range(1, 2):
        a_arr_row = len(a_arr)
        a_arr_column = len(a_arr[0])
        if a_arr_row >= a_arr_column:
            new_a_arr = [[] for _ in range(a_arr_row)]
            max_column = 0
            for i in range(a_arr_row):
                tmp_dict = defaultdict(int)
                for j in range(a_arr_column):
                    tmp_dict[a_arr[i][j]] += 1
                for key in tmp_dict:
                    if key != 0:
                        new_a_arr[i] += [key, tmp_dict[key]]
                if len(new_a_arr[i]) > max_column:
                    max_column = len(new_a_arr[i])
            for i in range(a_arr_row):
                if len(new_a_arr[i]) < max_column:
                    new_a_arr[i] += [0] * (max_column - len(new_a_arr[i]))
        else:
            for j in range(a_arr_column):
                tmp_dict = defaultdict(int)
                for i in range(a_arr_row):
                    tmp_dict[a_arr[i][j]] += 1
                
        if a_arr[r][c] == k:
            answer = t
            break'''
