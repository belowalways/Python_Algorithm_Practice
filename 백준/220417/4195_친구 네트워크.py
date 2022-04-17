import sys

n = int(sys.stdin.readline().rstrip())


def getParent(parent, x):
    if parent[x] == x:
        return x
    parent[x] = getParent(parent, parent[x])
    return parent[x]


def unionParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a == b:
        return
    if a < b:
        parent[b] = a
        cnt[a] += cnt[b]
    else:
        parent[a] = b
        cnt[b] += cnt[a]


def findRoot(parent, x):
    if parent[x] == x:
        return x
    else:
        return findRoot(parent, parent[x])

answer = []

for _ in range(n):
    f = int(sys.stdin.readline().rstrip())
    parent = {}
    cnt = {}
    for _ in range(f):
        friend_1, friend_2 = sys.stdin.readline().rstrip().split()
        if friend_1 not in parent:
            parent[friend_1] = friend_1
            cnt[friend_1] = 1
        if friend_2 not in parent:
            parent[friend_2] = friend_2
            cnt[friend_2] = 1
        unionParent(parent, friend_1, friend_2)
        answer.append(cnt[findRoot(parent, friend_1)])

for ans in answer:
    print(ans)

    '''i = 1
    int_dict = defaultdict(int)
    parent = [0]
    for _ in range(f):
        friend_1, friend_2 = input().split()
        if int_dict[friend_1] == 0:
            int_dict[friend_1] = i
            parent += [i]
            i += 1
        if int_dict[friend_2] == 0:
            int_dict[friend_2] = i
            parent += [i]
            i += 1
        unionParent(parent, int_dict[friend_1], int_dict[friend_2])
        count = 0
        for p in parent:
            if parent[int_dict[friend_1]] == getParent(parent, p):
                count += 1
        print(count)'''


'''for _ in range(n):
    f = int(input())
    friendship_arr = []
    for _ in range(f):
        next_friendship_arr = []
        friend_1, friend_2 = input().split()
        tmp_friendship = {friend_1, friend_2}
        for friendship in friendship_arr:
            if friend_1 in friendship or friend_2 in friendship:
                tmp_friendship = tmp_friendship | friendship
            else:
                next_friendship_arr.append(friendship)
        print(len(tmp_friendship))
        next_friendship_arr.append(tmp_friendship)
        friendship_arr = next_friendship_arr'''
