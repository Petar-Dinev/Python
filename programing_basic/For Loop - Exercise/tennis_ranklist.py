import math

count_of_tournaments = int(input())
start_points = int(input())

points_from_tournaments = 0
winnings = 0

for tournament in range(count_of_tournaments):
    result_from_tournament = input()

    if result_from_tournament == 'W':
        winnings += 1
        points_from_tournaments += 2000
    elif result_from_tournament == 'F':
        points_from_tournaments += 1200
    elif result_from_tournament == 'SF':
        points_from_tournaments += 720

average_points_per_tournament = points_from_tournaments / count_of_tournaments
percent_wins = winnings / count_of_tournaments * 100
total_points = start_points + points_from_tournaments

print(f"Final points: {total_points}")
print(f"Average points: {math.floor(average_points_per_tournament)}")
print(f"{percent_wins:.2f}%")
