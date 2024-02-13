num = int(input())
is_prime = True

for i in range(num - 1, 1, -1):
    if num % i == 0:
        is_prime = False

print(is_prime)
