username = input()
correct_password = input()
current_pass = input()

while current_pass != correct_password:
    current_pass = input()

print(f"Welcome {username}!")
