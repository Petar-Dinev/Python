messages_count = int(input())

for i in range(messages_count):
    message = ''
    code = int(input())
    if code == 88:
        message = 'Hello'
    elif code == 86:
        message = 'How are you?'
    elif code < 88 and code != 86:
        message = 'GREAT!'
    else:
        message = 'Bye.'
    print(message)
