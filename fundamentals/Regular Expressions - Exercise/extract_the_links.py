import re

pattern = r'(www\.[A-Za-z0-9-]+(\.[a-z]+)+)'

while True:
    line = input()
    if not line:
        break
    match = re.search(pattern, line)
    if match:
        print(match.group(1))
