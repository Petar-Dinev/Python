count_of_rooms = int(input())
count_of_free_chairs = 0
all_rooms_have_enough_chairs = True

for i in range(1, count_of_rooms + 1):
    room_info = input().split()
    chairs_in_room = len(room_info[0])
    guests = int(room_info[1])
    if chairs_in_room < guests:
        all_rooms_have_enough_chairs = False
        print(f"{guests - chairs_in_room} more chairs needed in room {i}")
    else:
        count_of_free_chairs += (chairs_in_room - guests)
if all_rooms_have_enough_chairs:
    print(f"Game On, {count_of_free_chairs} free chairs left")
