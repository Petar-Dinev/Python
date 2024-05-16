# text = input()
#
# characters = {}
#
# for char in text:
#     if char not in characters:
#         characters[char] = 0
#
#     characters[char] += 1
#
# sorted_characters = sorted(characters.keys())
# for char in sorted_characters:
#     print(f"{char}: {characters[char]} time/s")

text = input()
chars = set()

for char in text:
    chars.add(char)

sorted_chars = sorted(chars)
for char in sorted_chars:
    print(f"{char}: {text.count(char)} time/s")
