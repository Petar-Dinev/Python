heroes = {}
heroes_count = int(input())

for i in range(heroes_count):
    hero_info = input()
    name, hit_points, mana_points = hero_info.split()
    heroes[name] = {
        'hp': int(hit_points),
        'mp': int(mana_points)
    }

line = input()

while line != 'End':
    tokens = line.split(' - ')
    command = tokens[0]
    hero_name = tokens[1]
    hero = heroes[hero_name]

    if command == 'CastSpell':
        mana_needed = int(tokens[2])
        spell_name = tokens[3]
        if hero['mp'] >= mana_needed:
            hero['mp'] -= mana_needed
            print(f"{hero_name} has successfully cast {spell_name} and now has {hero['mp']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell_name}!")
    elif command == 'TakeDamage':
        damage = int(tokens[2])
        attacker = tokens[3]
        hero['hp'] -= damage
        if hero['hp'] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {hero['hp']} HP left!")
        else:
            print(f"{hero_name} has been killed by {attacker}!")
            del heroes[hero_name]
    elif command == 'Recharge':
        amount = int(tokens[2])
        current_mana = hero['mp']
        hero['mp'] += amount
        if hero['mp'] > 200:
            hero['mp'] = 200
            amount = 200 - current_mana
        print(f"{hero_name} recharged for {amount} MP!")
    else:
        amount = int(tokens[2])
        current_hit_points = hero['hp']
        hero['hp'] += amount
        if hero['hp'] > 100:
            hero['hp'] = 100
            amount = 100 - current_hit_points
        print(f"{hero_name} healed for {amount} HP!")

    line = input()

for current_hero_name, stats in heroes.items():
    print(current_hero_name)
    print(f"  HP: {stats['hp']}")
    print(f"  MP: {stats['mp']}")
