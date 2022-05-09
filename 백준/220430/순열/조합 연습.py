def permutations(arr, N):
    length = len(arr)
    result = []
    def dfs(visited, check_idx):
        if len(visited) == N:
            result.append(visited[:])
            return

        for idx in range(length):
            if idx not in check_idx:
                visited.append(arr[idx])
                check_idx.append(idx)
                dfs(visited, check_idx)
                check_idx.pop()
                visited.pop()

    dfs([], [])
    return result


def combinations(arr, N):
    length = len(arr)
    result = []

    def dfs(start_idx, visited):
        if len(visited) == N:
            result.append(visited[:])
            return

        for idx in range(start_idx, length):
            visited.append(arr[idx])
            dfs(idx + 1, visited)
            visited.pop()

    dfs(0, [])
    return result
