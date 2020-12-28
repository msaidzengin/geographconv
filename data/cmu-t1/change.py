import random
with open('user_info.test_eski', 'r', encoding='utf-8', errors='ignore') as f:
    content = f.readlines()
content = [x.strip() for x in content] 

chars = 'abcdefghijklmnoprqstuvwxyz 0123456789'
for i in range(len(content)):
    text = content[i].split('\t')[3].split(' ||| ')
    for i in range(int(len(text) * 0.1)):
        text[i] = text[i].replace(random.choice(text[i]), random.choice(chars))   
    text = ' ||| '.join(text)
    content[i] = '\t'.join(content[i].split('\t')[:3]) + '\t' + text
    
with open('user_info.test', 'w', encoding='utf-8') as f:
    for item in content:
        f.write(item + '\n')
