hour = int(input())
day = input()
is_open = False
if day != 'Sunday':
    if 10 <= hour <= 18:
        is_open = True
if is_open:
    print('open')
else:
    print('closed')
