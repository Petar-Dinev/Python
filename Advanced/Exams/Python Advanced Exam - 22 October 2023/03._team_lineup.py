def team_lineup(*args):
    players_by_country = {}

    for player, country in args:
        players_by_country[country] = players_by_country.get(country, []) + [player]

    result = []

    for country, players in sorted(players_by_country.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])):
        result.append(country + ':')
        for player in players:
            result.append(f"  -{player}")

    return '\n'.join(result)


print(team_lineup(
   ("Lionel Messi", "Argentina"),
   ("Neymar", "Brazil"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Harry Kane", "England"),
   ("Kylian Mbappe", "France"),
   ("Raheem Sterling", "England")))

