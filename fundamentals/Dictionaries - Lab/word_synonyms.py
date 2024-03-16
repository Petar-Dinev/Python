count_of_words = int(input())

words_dict = {}

for i in range(count_of_words):
    word = input()
    synonym = input()
    if word not in words_dict:
        words_dict[word] = []
    words_dict[word].append(synonym)

for key, value in words_dict.items():
    print(f"{key} - {', '.join(value)}")
