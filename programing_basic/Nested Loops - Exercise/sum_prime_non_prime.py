prime_sum = 0
not_prime_sum = 0

command = input()
while command != 'stop':
    current_num = int(command)
    if current_num < 0:
        command = input()
        print("Number is negative.")
        continue
    is_prime = True
    for num in range(current_num - 1, 1, -1):
        if current_num % num == 0:
            not_prime_sum += current_num
            is_prime = False
            break
    if is_prime:
        prime_sum += current_num
    command = input()

print(f"Sum of all prime numbers is: {prime_sum}")
print(f"Sum of all non prime numbers is: {not_prime_sum}")
