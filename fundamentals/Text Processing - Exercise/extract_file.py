path = input()
path_tokens = path.split('\\')
name_of_file, extension = path_tokens[-1].split('.')

print(f"File name: {name_of_file}")
print(f"File extension: {extension}")