cards = input().split(' ')
teamA = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
teamB = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
game_is_terminated = False

for card in cards:
    team, player = card.split('-')
    player = int(player)
    if team == 'A':
        if player in teamA:
            teamA.remove(player)
    elif team == 'B':
        if player in teamB:
            teamB.remove(player)
    if len(teamA) < 7 or len(teamB) < 7:
        game_is_terminated = True
        break
print(f"Team A - {len(teamA)};", end=" ")
print(f"Team B - {len(teamB)}")

if game_is_terminated:
    print("Game was terminated")
