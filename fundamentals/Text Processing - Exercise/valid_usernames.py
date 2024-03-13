def check_name(user_name):
    if len(user_name) < 3 or len(user_name) > 16:
        return False
    for char in user_name:
        if not (char.isalnum() or char == '-' or char == '_'):
            return False
    if ' ' in user_name:
        return False
    return True


names = input().split(', ')

for name in names:
    if check_name(name):
        print(name)
