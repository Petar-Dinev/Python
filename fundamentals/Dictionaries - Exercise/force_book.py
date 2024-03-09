sides = {}
command = input()

while command != 'Lumpawaroo':
    if '|' in command:
        side, user = command.split(' | ')
        has_user = False
        for side_ in sides.keys():
            if user in sides[side_]:
                has_user = True
        if not has_user:
            if side not in sides:
                sides[side] = []
            if user not in sides[side]:
                sides[side].append(user)
    else:
        user, side = command.split(' -> ')
        has_user = False
        for side_ in sides.keys():
            if user in sides[side_]:
                has_user = True

        if not has_user:
            if side not in sides:
                sides[side] = []
            if user not in sides[side]:
                sides[side].append(user)
                print(f"{user} joins the {side} side!")
        else:
            for side_ in sides.keys():
                if user in sides[side_] and side_ != side:
                    sides[side_].remove(user)
            if side not in sides:
                sides[side] = []
            if user not in sides[side]:
                sides[side].append(user)
                print(f"{user} joins the {side} side!")
    command = input()

for side, members in sides.items():
    if len(members) > 0:
        print(f'Side: {side}, Members: {len(members)}')
        for member in members:
            print(f'! {member}')
