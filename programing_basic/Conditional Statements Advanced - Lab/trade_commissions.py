town = input()
sells = float(input())
percent = 0
is_error = False
if sells < 0:
    is_error = True
else:
    if town == 'Sofia':
        if sells <= 500:
            percent = 5
        elif sells <= 1000:
            percent = 7
        elif sells <= 10000:
            percent = 8
        else:
            percent = 12
    elif town == 'Varna':
        if sells <= 500:
            percent = 4.5
        elif sells <= 1000:
            percent = 7.5
        elif sells <= 10000:
            percent = 10
        else:
            percent = 13
    elif town == 'Plovdiv':
        if sells <= 500:
            percent = 5.5
        elif sells <= 1000:
            percent = 8
        elif sells <= 10000:
            percent = 12
        else:
            percent = 14.5
    else:
        is_error = True

if is_error:
    print('error')
else:
    profit = sells * percent / 100
    print(f"{profit:.2f}")
