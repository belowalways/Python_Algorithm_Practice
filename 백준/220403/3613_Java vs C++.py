import re

i = input()

java = re.compile('[a-z]+(([A-Z]([a-z]*)?)*)?')
cplusplus = re.compile('[a-z]+((_[a-z]+)*)?')

if java.fullmatch(i):
    print(re.sub('[A-Z]([a-z]*)?', lambda mat: '_' + mat.group(0).lower(), i))
elif cplusplus.fullmatch(i):
    print(re.sub('_([a-z])', lambda mat: mat.group(1).upper(), i))
else:
    print("Error!")
