# 왜 틀렸지 ?

html_str = input()
html_len = len(html_str)
tmp_str = ""
i = 0
html_list = []

while i < html_len:
    tmp_char = html_str[i]
    if tmp_char == '<':
        if tmp_str != "":
            html_list.append("*" + tmp_str)
        tmp_str = ""
    elif tmp_char == '>':
        html_list.append(tmp_str)
        tmp_str = ""
    else:
        tmp_str += html_str[i]
    i += 1

paragraph_start = False
p_str = ""

for html in html_list:
    if html[:3] == "div":
        print("title : " + html[11:-1])
    elif html == "p":
        paragraph_start = True
    elif html == "/p":
        p_str = p_str.rstrip()
        p_str = p_str.lstrip()

        while "  " in p_str:
            p_str = p_str.replace("  ", " ")

        print(p_str)
        p_str = ""
        paragraph_start = False
    elif paragraph_start and len(html) > 1:
        if html[0] == "*":
            p_str += html[1:]
