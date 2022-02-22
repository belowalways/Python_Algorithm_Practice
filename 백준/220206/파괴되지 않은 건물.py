'''def solution(board, skill):
    n = len(board)
    m = len(board[0])

    answer = 0

    for turn in skill:
        _type, r1, c1, r2, c2, degree = turn[0], turn[1], turn[2], turn[3], turn[4], turn[5]
        if _type == 1:
            degree = -degree

        for i in range(r1, r2 + 1):
            for j in range(c1, c2 + 1):
                board[i][j] += degree

    for x in range(n):
        for y in range(m):
            if board[x][y] > 0:
                answer += 1

    return answer'''
