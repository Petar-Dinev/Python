string = input()
words_to_find = ["sand", "water", "fish", "sun"]
find_words_count = 0

current_word = ''

for char in string:
    current_word += char.lower()
    for i in range(len(words_to_find)):
        if words_to_find[i] in current_word:
            find_words_count += 1
            current_word = ''

print(find_words_count)
