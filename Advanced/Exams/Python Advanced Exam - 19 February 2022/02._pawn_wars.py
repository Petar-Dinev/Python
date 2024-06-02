chest_board_size = 8
chest_board, w_row, w_col, b_row, b_col = [], 0, 0, 0, 0

for row in range(chest_board_size):
    chest_board.append(input().split())
    for col in range(chest_board_size):
        if chest_board[row][col] == 'w':
            w_row, w_col = row, col
        elif chest_board[row][col] == 'b':
            b_row, b_col = row, col


while True:
    if (w_row - 1, w_col - 1) == (b_row, b_col) or (w_row - 1, w_col + 1) == (b_row, b_col):
        print(f"Game over! White win, capture on {chr(97 + b_col)}{chest_board_size - b_row}.")
        break

    w_row -= 1

    if w_row == 0:
        print(f"Game over! White pawn is promoted to a queen at {chr(97 + w_col)}8.")
        break

    if (b_row + 1, b_col - 1) == (w_row, w_col) or (b_row + 1, b_col + 1) == (w_row, w_col):
        print(f"Game over! Black win, capture on {chr(97 + w_col)}{chest_board_size - w_row}.")
        break

    b_row += 1

    if b_row == chest_board_size - 1:
        print(f"Game over! Black pawn is promoted to a queen at {chr(97 + b_col)}1.")
        break
