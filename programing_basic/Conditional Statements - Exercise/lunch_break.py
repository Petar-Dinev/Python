import math

name_of_tv_series = input()
time_on_tv_episode = int(input())
break_time = int(input())

lunch_time = break_time / 8
rest_time = break_time / 4
left_time = break_time - lunch_time - rest_time
difference = math.ceil(abs(left_time - time_on_tv_episode))

if left_time >= time_on_tv_episode:
    print(f"You have enough time to watch {name_of_tv_series} and left with {difference} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_tv_series}, you need {difference} more minutes.")
