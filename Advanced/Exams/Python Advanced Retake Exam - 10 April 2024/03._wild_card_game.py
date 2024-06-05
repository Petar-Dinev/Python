def draw_cards(*args, **kwargs):
    monster_cards = []
    spell_cards = []

    for data in args:
        if data[1] == 'monster':
            monster_cards.append(data[0])
        else:
            spell_cards.append(data[0])

    for data in kwargs.items():
        if data[1] == 'monster':
            monster_cards.append(data[0])
        else:
            spell_cards.append(data[0])

    result = []

    if monster_cards:
        result.append("Monster cards:")
        for monster in sorted(monster_cards, reverse=True):
            result.append(f"  ***{monster}")

    if spell_cards:
        result.append("Spell cards:")
        for spell in sorted(spell_cards):
            result.append(f"  $$${spell}")

    return '\n'.join(result)


print(draw_cards(("cyber dragon", "monster"), freeze="spell",))
print(draw_cards(("celtic guardian", "monster"), ("earthquake", "spell"),
                 ("fireball", "spell"), raigeki="spell", destroy="spell",))
