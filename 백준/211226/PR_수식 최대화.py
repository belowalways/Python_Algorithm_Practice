import math
import copy


def operate(x, y, op):
    if op == '+':
        return x + y
    if op == '-':
        return x - y
    if op == '*':
        return x * y


def solution(expression):
    operator = []
    operand = []
    _expression = expression[:]

    idx = 0

    while len(_expression) > 0:

        if _expression[idx] == '-' or _expression[idx] == '+' or _expression[idx] == '*':
            operator.append(_expression[idx])
            operand.append(int(_expression[:idx]))
            _expression = _expression[idx + 1:]
            idx = 0

        if len(_expression) == idx + 1:
            operand.append(int(_expression))
            break

        idx += 1

    rank_list = [['+', '-', '*'], ['+', '*', '-'], ['-', '+', '*'],
                 ['-', '*', '+'], ['*', '-', '+'], ['*', '+', '-']]

    answer = -1
    answer_list = []

    for rank in rank_list:
        _operator = copy.deepcopy(operator)
        _operand = copy.deepcopy(operand)

        for r in rank:
            op_idx = 0
            while op_idx < len(_operator):
                if _operator[op_idx] == r:
                    _operand[op_idx + 1] = operate(_operand[op_idx], _operand[op_idx + 1], r)
                    _operand.remove(_operand[op_idx])
                    _operator.remove(_operator[op_idx])
                    continue
                op_idx += 1

        answer_list.append(_operand[0])
        if math.fabs(_operand[0]) > answer:
            answer = math.fabs(_operand[0])

    return answer