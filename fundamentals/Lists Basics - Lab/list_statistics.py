count_of_numbers = int(input())

positive_numbers = []
negative_numbers = []

for i in range(count_of_numbers):
    num = int(input())
    if num < 0:
        negative_numbers.append(num)
    else:
        positive_numbers.append(num)

print(positive_numbers)
print(negative_numbers)
print(f"Count of positives: {len(positive_numbers)}")
print(f"Sum of negatives: {sum(negative_numbers)}")
