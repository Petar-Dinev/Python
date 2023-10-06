count_of_groups = int(input())

peak_musala_counter = 0
peak_monblan_counter = 0
peak_kilimajaro_counter = 0
peak_k2_counter = 0
peak_everest_counter = 0
total_climbers = 0

for group in range(count_of_groups):
    current_group_count = int(input())
    total_climbers += current_group_count

    if current_group_count <= 5:
        peak_musala_counter += current_group_count
    elif current_group_count <= 12:
        peak_monblan_counter += current_group_count
    elif current_group_count <= 25:
        peak_kilimajaro_counter += current_group_count
    elif current_group_count <= 40:
        peak_k2_counter += current_group_count
    else:
        peak_everest_counter += current_group_count

percent_of_musala = peak_musala_counter / total_climbers * 100
percent_of_monblan = peak_monblan_counter / total_climbers * 100
percent_of_kilimanjaro = peak_kilimajaro_counter / total_climbers * 100
percent_of_k2 = peak_k2_counter / total_climbers * 100
percent_of_everest = peak_everest_counter / total_climbers * 100

print(f"{percent_of_musala:.2f}%")
print(f"{percent_of_monblan:.2f}%")
print(f"{percent_of_kilimanjaro:.2f}%")
print(f"{percent_of_k2:.2f}%")
print(f"{percent_of_everest:.2f}%")

