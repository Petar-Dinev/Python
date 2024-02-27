people_waiting = int(input())
state_of_the_lift = [int(num) for num in input().split()]
spots_on_lift = len(state_of_the_lift) * 4
empty_spots_on_lift = spots_on_lift - sum(state_of_the_lift)

while people_waiting > 0 and empty_spots_on_lift != 0:

    for i in range(len(state_of_the_lift)):
        if people_waiting >= 4:
            current_available_spots = 4 - state_of_the_lift[i]
        else:
            current_available_spots = people_waiting

        state_of_the_lift[i] += current_available_spots
        people_waiting -= current_available_spots
        empty_spots_on_lift -= current_available_spots

if empty_spots_on_lift > 0:
    print('The lift has empty spots!')
if people_waiting > 0:
    print(f"There isn't enough space! {people_waiting} people in a queue!")
print(" ".join([str(num) for num in state_of_the_lift]))
