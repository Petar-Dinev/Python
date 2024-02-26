first_line = input().split()
second_line = input().split()
third_line = input().split()
first_player_won = False
second_player_won = False

for i in range(3):
    for k in range(3):
        for l in range(3):
            if i == k == l:
                if first_line[i] == second_line[k] == third_line[l]:
                    if first_line[i] == '1':
                        first_player_won = True
                    elif first_line[i] == '2':
                        second_player_won = True
            elif (i == 0 and k == 1 and l == 2) or (i == 2 and k == 1 and l == 0):
                if first_line[i] == second_line[k] == third_line[l]:
                    if first_line[i] == '1':
                        first_player_won = True
                    elif first_line[i] == '2':
                        second_player_won = True
                elif first_line[i] == first_line[k] == first_line[l]:
                    if first_line[i] == '1':
                        first_player_won = True
                    elif first_line[i] == '2':
                        second_player_won = True
                elif second_line[i] == second_line[k] == second_line[l]:
                    if second_line[i] == '1':
                        first_player_won = True
                    elif second_line[i] == '2':
                        second_player_won = True
                elif third_line[i] == third_line[k] == third_line[l]:
                    if third_line[i] == '1':
                        first_player_won = True
                    elif third_line[i] == '2':
                        second_player_won = True
if first_player_won:
    print("First player won")
elif second_player_won:
    print("Second player won")
else:
    print("Draw!")
