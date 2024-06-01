from collections import deque

vowels = deque(input().split())
consonants = input().split()

search_words = ['rose', 'tulip', 'lotus', 'daffodil']
used_letters = []

is_found = False
word_found = ''

while not is_found and vowels and consonants:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()

    for word in search_words:
        if current_vowel in word:
            used_letters.append(current_vowel)
        if current_consonant in word:
            used_letters.append(current_consonant)

        for character in word:
            if character not in used_letters:
                break
        else:
            is_found = True
            word_found = word

if is_found:
    print(f"Word found: {word_found}")
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
