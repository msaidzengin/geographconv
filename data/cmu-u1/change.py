import random
with open('user_info.test_eski', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.readlines()
content = [x.strip() for x in content] 

lines = {}
chars = 'abcdefghijklmnoprqstuvwxyz 0123456789'
for i in range(len(content)):
    text = content[i].split('\t')[3].split(' ||| ')
    lines[content[i]] = len(text)

lines = dict(sorted(lines.items(), key=lambda item: item[1]))
lines = list(lines.keys())

size = len(lines) // 5
list1 = lines[size * 0 : size * 1]
list2 = lines[size * 1 : size * 2]
list3 = lines[size * 2 : size * 3]
list4 = lines[size * 3 : size * 4]
list5 = lines[size * 4 : size * 5]

with open('user_info.test1', 'w', encoding='utf-8') as f:
    for item in list1:
        f.write(item + '\n')

with open('user_info.test2', 'w', encoding='utf-8') as f:
    for item in list2:
        f.write(item + '\n')

with open('user_info.test3', 'w', encoding='utf-8') as f:
    for item in list3:
        f.write(item + '\n')

with open('user_info.test4', 'w', encoding='utf-8') as f:
    for item in list4:
        f.write(item + '\n')

with open('user_info.test5', 'w', encoding='utf-8') as f:
    for item in list5:
        f.write(item + '\n')