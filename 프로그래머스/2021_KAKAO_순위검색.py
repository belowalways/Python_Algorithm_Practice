def solution(info, query):
    for i in range(len(query)):
        query[i] = query[i].split(" and ")
        temp = query[i][3].split(' ')
        query[i][3] = temp[0]
        query[i].append(temp[1])

    for j in range(len(info)):
        info[j] = info[j].split(' ')

    answer = [0] * len(query)

    for m in range(len(query)):
        for k in range(len(info)):
            cnt = 0
            for n in range(4):
                if info[k][n] == query[m][n] or query[m][n] == '-':
                    cnt += 1
                else:
                    break
            if int(info[k][4]) >= int(query[m][4]) and cnt == 4:
                answer[m] += 1

    return answer

# 효율성 실패