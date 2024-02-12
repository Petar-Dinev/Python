num_of_lines = int(input())
is_balanced = True
current_bracket = ''

for i in range(num_of_lines):

    current_input = input()

    if current_input == '(' or current_input == ')':
        if current_bracket == '':
            if current_input == ')':
                is_balanced = False
                break
            current_bracket = current_input
        else:
            current_bracket += current_input

            if current_bracket == '()':
                is_balanced = True
                current_bracket = ''
            else:
                is_balanced = False
                break

if is_balanced:
    print('BALANCED')
else:
    print('UNBALANCED')
