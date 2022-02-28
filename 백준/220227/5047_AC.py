from collections import deque


def print_answer(function_str, n, list_str):
    is_reverse = False

    if n != 0:
        list_str = list_str[1:-1]
        if list_str.count(',') > 0:
            queue = deque(list(map(int, list_str.split(','))))
        else:
            queue = deque([int(list_str)])
    else:
        queue = deque([])

    for function in function_str:
        if function == 'D':
            if len(queue) == 0:
                print("error")
                return
            if is_reverse:
                queue.pop()
            else:
                queue.popleft()
        else:
            is_reverse = not is_reverse

    answer_string = ""

    if is_reverse:
        answer_list = list(queue)[::-1]
    else:
        answer_list = list(queue)

    for answer in answer_list:
        answer_string += (str(answer) + ",")

    answer_string = "[" + answer_string[:-1] + "]"

    print(answer_string)


T = int(input())

for _ in range(T):
    function_str = input()
    n = int(input())
    list_str = input()
    print_answer(function_str, n, list_str)
