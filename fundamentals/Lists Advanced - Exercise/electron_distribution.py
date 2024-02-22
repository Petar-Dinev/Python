electrons = int(input())
shell_position = 1
shell = []

while electrons > 0:
    need_electrons_for_current_position = 2 * (shell_position ** 2)
    if electrons >= need_electrons_for_current_position:
        shell.append(need_electrons_for_current_position)
        electrons -= need_electrons_for_current_position
    else:
        shell.append(electrons)
        electrons = 0
    shell_position += 1

print(shell)
