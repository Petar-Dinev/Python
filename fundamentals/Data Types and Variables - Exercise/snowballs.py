number_of_snowballs = int(input())

most_value_of_snowball = 0
data_of_highest_snowball_value = {}
for current_snowball in range(number_of_snowballs):
    weight_of_snowball = int(input())
    time_for_made_snowball = int(input())
    quality_of_snowball = int(input())
    current_snowball_value = int(weight_of_snowball / time_for_made_snowball) ** quality_of_snowball

    if current_snowball_value > most_value_of_snowball:
        most_value_of_snowball = current_snowball_value
        data_of_highest_snowball_value = {
            'snowball_weight': weight_of_snowball,
            'snowball_time': time_for_made_snowball,
            'snowball_quality': quality_of_snowball,
            'snowball_value': most_value_of_snowball
        }
print(f"{data_of_highest_snowball_value['snowball_weight']} : {data_of_highest_snowball_value['snowball_time']} \
= {data_of_highest_snowball_value['snowball_value']} ({data_of_highest_snowball_value['snowball_quality']})")
