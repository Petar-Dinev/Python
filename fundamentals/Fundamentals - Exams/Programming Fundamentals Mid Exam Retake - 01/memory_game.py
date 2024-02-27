sequence = input().split()

current_input_line = input()
moves = 0

while current_input_line != 'end':
    middle_of_sequence = len(sequence) // 2
    first_index, second_index = current_input_line.split()
    first_index = int(first_index)
    second_index = int(second_index)
    moves += 1

    if first_index == second_index or not 0 <= first_index < len(sequence) or not 0 <= second_index < len(sequence):
        el_to_insert = f'-{moves}a'
        sequence.insert(middle_of_sequence, el_to_insert)
        sequence.insert(middle_of_sequence, el_to_insert)
        print("Invalid input! Adding additional elements to the board")
    else:
        if sequence[first_index] == sequence[second_index]:
            print(f"Congrats! You have found matching elements - {sequence[first_index]}!")
            sequence = [el for i, el in enumerate(sequence) if i != first_index and i != second_index]
        else:
            print("Try again!")

    current_input_line = input()

    if not sequence:
        print(f"You have won in {moves} turns!")
        break
else:
    print(f"Sorry you lose :(\n{' '.join(sequence)}")
