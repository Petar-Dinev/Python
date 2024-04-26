contests = {}

line = input()

while line != 'end of contests':
    contest, password = line.split(":")
    contests[contest] = {'password': password}

    line = input()

users = {}
line = input()

while line != 'end of submissions':
    contest, password, username, points = line.split('=>')
    points = int(points)
    if contest in contests:
        if contests[contest]['password'] == password:
            if username not in users:
                users[username] = {}
            if contest not in users[username]:
                users[username][contest] = points
            else:
                if users[username][contest] < points:
                    users[username][contest] = points
    line = input()

most_points = 0
most_points_user = None

for user in users:
    user_points = sum(users[user].values())
    if user_points > most_points:
        most_points = user_points
        most_points_user = user

print(f"Best candidate is {most_points_user} with total {most_points} points.")
print('Ranking:')

for user in sorted(users.keys()):
    print(user)
    for contest, points in sorted(users[user].items(), key=lambda c: -c[1]):
        print(f"#  {contest} -> {points}")
