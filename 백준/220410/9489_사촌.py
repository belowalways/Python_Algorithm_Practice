while True:
    n, k = map(int, input().split(' '))
    if n == 0 and k == 0:
        break
    # print("n, k =", str(n) + ",", k)
    node_list = list(map(int, input().split(' ')))

    '''seq_list = [node_list[0]]
    tree = []

    for i in range(1, n):
        if node_list[i] == node_list[i - 1] + 1:
            seq_list.append(node_list[i])
        else:
            tree.append(seq_list)
            seq_list = [node_list[i]]

    tree.append(seq_list)

    print(tree)'''

    seq_list = [1]
    tree = []

    for i in range(1, n):
        if node_list[i] == node_list[i - 1] + 1:
            seq_list.append(i + 1)
        else:
            tree.append(seq_list)
            seq_list = [i + 1]

    tree.append(seq_list)
    k_idx = node_list.index(k)
    #print(node_list.index(k))
    answer = 0

    for i in range(len(tree)):
        if k_idx + 1 in tree[i]:
            answer -= len(tree[i])
            for j in range(len(tree)):
                if i in tree[j]:
                    #print(tree[j], "# 부모 및 형제 리스트")
                    for index in tree[j]:
                        if index < len(tree):
                            answer += len(tree[index])
            if answer > 0:
                print(answer)
            else:
                print(0)
            break

    #print(tree)







    '''    parent_list = [-1] * n
    tree = []
    waiting_child = deque([])
    next_waiting_child = deque([node_list[0]])
    waiting_child_node = -1
    
    for i in range(1, n):
        if node_list[i] == node_list[i - 1] + 1:
            next_waiting_child.append(node_list[i])
        else:
            if len(waiting_child) == 0:
                waiting_child = next_waiting_child
                next_waiting_child = deque([])
            waiting_child_node = waiting_child.popleft()
            next_waiting_child.append(node_list[i])
        parent_list[i] = waiting_child_node'''

    '''k_idx = node_list.index(k)
    parent_node = parent_list[k_idx]
    if parent_node == node_list[0] or parent_node == -1:
        print(0)
        continue

    grandparent_node = parent_list[node_list.index(parent_list[k_idx])]

    idx = depth.index(depth[k_idx])
    cousin_count = 0
    while idx < n:
        if depth[idx] > depth[k_idx]:
            break
        if parent_node == parent_list[idx]:
            idx += 1
        elif grandparent_node == parent_list[node_list.index(parent_list[idx])]:
            cousin_count += 1
            idx += 1

    print(cousin_count)'''




