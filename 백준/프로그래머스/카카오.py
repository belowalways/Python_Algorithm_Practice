info = ["java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"]

query = ["java and backend and junior and pizza 100",
         "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250",
         "- and backend and senior and - 150",
         "- and - and - and chicken 100",
         "- and - and - and - 150"]

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

print(answer)

# 딕셔녀리로 풀기

