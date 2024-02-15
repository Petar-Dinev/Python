def print_loading_bar(percent):
    percent_count = percent // 10
    dot_count = 10 - percent_count
    percent_string = '%' * percent_count
    dot_string = '.' * dot_count

    if percent == 100:
        print('100% Complete!')
        print('[%%%%%%%%%%]')
    else:
        print(f'{percent}% [{percent_string}{dot_string}]')
        print('Still loading...')


num = int(input())
print_loading_bar(num)
