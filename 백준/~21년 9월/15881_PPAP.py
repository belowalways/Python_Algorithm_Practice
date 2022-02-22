n = int(input())

input_str = input()
cnt = 0

edited_str = input_str.replace("pPAp", '')

print(int((n - len(edited_str))/4))