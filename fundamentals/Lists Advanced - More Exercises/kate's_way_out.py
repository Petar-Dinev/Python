maze_size = int(input())

maze = []
kate_position = []
exits = []

for row in range(maze_size):
    current_row = list(input())
    if row == 0 or row == maze_size - 1:
        for position in range(len(current_row)):
            if current_row[position] == ' ':
                exits.append((row, position))
    else:
        if current_row[0] == ' ':
            exits.append((row, 0))
        if current_row[-1] == ' ':
            exits.append((row, len(current_row) - 1))

    maze.append(current_row)
    if 'k' in current_row:
        kate_position = [row, current_row.index('k')]

max_moves = 0
it_is_escaped = False

for i in range(maze_size):
    if i == 0 or i == maze_size - 1:
        for el in maze[i]:
            if el == 'k':
                max_moves = 1
                it_is_escaped = True

    else:
        if maze[i][0] == 'k' or maze[i][-1] == 'k':
            max_moves = 1
            it_is_escaped = True

moves = [(-1, 0), (0, 1), (1, 0), (0, -1)]

for exit_row, exit_col in exits:
    current_moves = 0
    visited_positions = [(exit_row, exit_col)]
    is_escaped = False

    current_row, current_col = exit_row, exit_col

    while True:
        is_moved = False

        for row, col in moves:
            new_row = current_row + row
            new_col = current_col + col

            if 0 <= new_row < len(maze) and 0 <= new_col < len(maze[new_row]) and (new_row, new_col) \
                    not in visited_positions and maze[new_row][new_col] != '#':
                visited_positions.append((new_row, new_col))
                current_row, current_col = new_row, new_col
                current_moves += 1
                is_moved = True

                if maze[new_row][new_col] == 'k':
                    is_escaped = True
                    break

                if is_moved:
                    break

        if is_escaped or not is_moved:
            break

    current_moves += 1
    if current_moves > max_moves:
        max_moves = current_moves
    if is_escaped:
        it_is_escaped = True

if it_is_escaped:
    print(f"Kate got out in {max_moves} moves")
else:
    print("Kate cannot get out")
