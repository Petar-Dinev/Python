count_of_pieces = int(input())
pieces = {}

for i in range(count_of_pieces):
    current_piece_info = input().split('|')
    name_of_piece, composer, key = current_piece_info
    pieces[name_of_piece] = {
        'composer': composer,
        'key': key
    }

line = input()

while line != 'Stop':
    tokens = line.split('|')
    command = tokens[0]
    current_piece_name = tokens[1]
    current_piece = {}
    if current_piece_name in pieces:
        current_piece = pieces[current_piece_name]

    if command == 'Add':
        composer = tokens[2]
        key = tokens[3]
        if current_piece_name not in pieces:
            pieces[current_piece_name] = {
                'composer': composer,
                'key': key
            }
            print(f"{current_piece_name} by {composer} in {key} added to the collection!")
        else:
            print(f"{current_piece_name} is already in the collection!")
    elif command == 'Remove':
        if current_piece_name in pieces:
            del pieces[current_piece_name]
            print(f"Successfully removed {current_piece_name}!")
        else:
            print(f"Invalid operation! {current_piece_name} does not exist in the collection.")
    else:
        new_key = tokens[2]
        if current_piece_name in pieces:
            current_piece['key'] = new_key
            print(f"Changed the key of {current_piece_name} to {new_key}!")
        else:
            print(f"Invalid operation! {current_piece_name} does not exist in the collection.")
    line = input()

for piece, piece_info in pieces.items():
    print(f"{piece} -> Composer: {piece_info['composer']}, Key: {piece_info['key']}")
