parentheses = input()
stack = []
is_balanced = True

for i in range(len(parentheses)):
    if parentheses[i] == '(' or parentheses[i] == '{' or parentheses[i] == '[':
        stack.append(parentheses[i])
    else:
        if len(stack) > 0:
            if (parentheses[i] == ')' and stack[-1] == '(') or (parentheses[i] == '}' and stack[-1] == '{') or \
                    (parentheses[i] == ']' and stack[-1] == '['):
                stack.pop()
            else:
                is_balanced = False
                break
        else:
            is_balanced = False
            break

if is_balanced:
    print('YES')
else:
    print('NO')
