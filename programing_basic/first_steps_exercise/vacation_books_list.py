from math import floor
pages = int(input())
pages_for_hour = int(input())
days = int(input())
hours_for_read_per_day = floor(pages / pages_for_hour) / days
print(hours_for_read_per_day)