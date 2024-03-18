import re

names = input()

pattern = r'\b[A-Z][a-z]{1,}\s[A-Z][a-z]{1,}\b'

matches = re.findall(pattern, names)

print(' '.join(matches))
