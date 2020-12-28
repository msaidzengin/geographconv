with open('user_info.test', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.readlines()
content = [x.strip() for x in content] 

for i in range(len(content)):
    content[i] = content[i] + ' ||| I love Istanbul. Istanbul is a very nice city!'

with open('new.txt', 'w', encoding='utf-8') as f:
    for item in content:
        f.write(item + '\n')
