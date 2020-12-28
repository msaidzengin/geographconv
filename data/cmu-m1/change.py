import random
with open('user_info.test_eski', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.readlines()
content = [x.strip() for x in content] 

for i in range(len(content)):
    line = random.choice(content)
    user = line.split('\t')[0]
    content[i] = content[i] + ' ||| ' + user + ' I love Istanbul. Istanbul is a very nice city!'

with open('user_info.test', 'w', encoding='utf-8') as f:
    for item in content:
        f.write(item + '\n')
