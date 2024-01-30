count_of_strings = int(input())
search_word = input()
list_of_strings = []
search_list = []

for i in range(count_of_strings):
    list_of_strings.append(input())

for string in list_of_strings:
    if search_word in string:
        search_list.append(string)

print(list_of_strings)
print(search_list)
