count_of_numbers = int(input())

p1_count = 0
p2_count = 0
p3_count = 0
p4_count = 0
p5_count = 0

for num in range(count_of_numbers):
    current_num = int(input())

    if current_num < 200:
        p1_count +=1
    elif current_num < 400:
        p2_count += 1
    elif current_num < 600:
        p3_count += 1
    elif current_num < 800:
        p4_count += 1
    else:
        p5_count += 1

p1_percent = p1_count / count_of_numbers * 100
p2_percent = p2_count / count_of_numbers * 100
p3_percent = p3_count / count_of_numbers * 100
p4_percent = p4_count / count_of_numbers * 100
p5_percent = p5_count / count_of_numbers * 100

print(f"{p1_percent:.2f}%")
print(f"{p2_percent:.2f}%")
print(f"{p3_percent:.2f}%")
print(f"{p4_percent:.2f}%")
print(f"{p5_percent:.2f}%")
