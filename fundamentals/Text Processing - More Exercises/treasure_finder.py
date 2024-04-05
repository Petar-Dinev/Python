keys = [int(num) for num in input().split()]
current_string = input()

while current_string != 'find':
    message = ''
    current_string_length = len(current_string)
    current_key_index = 0
    for i in range(current_string_length):
        if current_key_index >= len(keys):
            current_key_index = 0
        current_char = current_string[i]
        message += chr(ord(current_char) - keys[current_key_index])
        current_key_index += 1
    treasure_start_index = message.index('&') + 1
    treasure_end_index = message.index('&', treasure_start_index)
    coordinates_start_index = message.index('<') + 1
    coordinates_end_index = message.index('>')
    treasure = message[treasure_start_index:treasure_end_index]
    coordinates = message[coordinates_start_index:coordinates_end_index]
    print(f"Found {treasure} at {coordinates}")
    current_string = input()
