while True:
    word = input()
    if word == 'end':
        break
    reverse_word = word[::-1]
    print(f"{word} = {reverse_word}")
