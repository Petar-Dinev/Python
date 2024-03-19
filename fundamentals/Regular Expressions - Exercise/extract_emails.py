import re

sentence = input()
pattern = r'\s(([a-z0-9]+)([\.\_\-]*[a-z0-9])*@([a-z]+(\-*[a-z]+)*)(\.([a-z]+\-*[a-z]+))+)\b'

matches = re.findall(pattern, sentence)
for match in matches:
    print(match[0])
