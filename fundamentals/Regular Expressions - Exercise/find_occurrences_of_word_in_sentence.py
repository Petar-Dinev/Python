import re

sentence = input()
search_word = input()

pattern = fr"\b{search_word}\b"
matches = re.findall(pattern, sentence, re.I)

print(len(matches))
