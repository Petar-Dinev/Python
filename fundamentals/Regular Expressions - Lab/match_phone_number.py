import re

text = input()
pattern = r'(\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b)'
phones = re.findall(pattern, text)
print(', '.join(phones))
