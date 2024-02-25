strings = input().split()
search_palindrome = input()
found_palindromes = []
count_of_search_palindrome = 0

for string in strings:
    current_string_reverse = string[::-1]
    if string == current_string_reverse:
        found_palindromes.append(current_string_reverse)
    if current_string_reverse == search_palindrome:
        count_of_search_palindrome += 1

print(found_palindromes)
print(f"Found palindrome {count_of_search_palindrome} times")
