# 1114번 통나무 자르기

from collections import deque

L, K, C = map(int, input().split())

k_list = list(map(int, input().split()))

print(L, K, C)
print(k_list)

all_list = []

for i in k_list:
    all_list.append([i, [L - i, i]])  # [처음 자르는 위치, [조각 리스트]]

print(all_list)

for i in range(C - 1):  # 한 번 잘랐으니 C - 1번만 자를 수 있음
    tmp = all_list.pop()
    # 리스트 언패킹
    tmp_location = tmp[0]
    piece_list = tmp[1]

    for _ in range(len(piece_list)):  # piece_list만큼 반복

        for j in range(K):

            if piece_list[-1] > k_list[j]:  # 조각 리스트 중에 가장 큰 수가 k_list[j]보다 크면

                tmp = piece_list.pop()
                piece_list.append(k_list[j])
                piece_list.append(tmp - k_list[j])

                piece_list.sort()  # 조각 리스트 정렬

                all_list.append(tree_list)

print(all_list)

max_list = []

for k in range(len(all_list)):
    max_list.append(all_list[k].max())

print(max_list.min())
