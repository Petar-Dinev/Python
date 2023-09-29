actor_name = input()
starting_points_of_actor = float(input())
count_of_jury = int(input())

total_actor_points = starting_points_of_actor

for num in range(count_of_jury):
    current_jury_person = input()
    current_points = float(input())

    total_actor_points += int(len(current_jury_person)) * current_points / 2
    if total_actor_points > 1250.5:
        print(f"Congratulations, {actor_name} got a nominee for leading role with {total_actor_points:.1f}!")
        break

if total_actor_points <= 1250.5:
    difference = 1250.5 - total_actor_points
    print(f"Sorry, {actor_name} you need {difference:.1f} more!")
