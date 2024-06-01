def cookbook(*args):
    cookbook_dict = {}

    for data in args:
        recipe_name, cuisine, ingredients = data

        if cuisine not in cookbook_dict:
            cookbook_dict[cuisine] = {}

        cookbook_dict[cuisine][recipe_name] = ingredients

    result = []
    sorted_cookbook_dict = sorted(cookbook_dict.items(), key=lambda kvp: (-len(kvp[1]), kvp[0]))

    for cuisine, recipes in sorted_cookbook_dict:
        result.append(f"{cuisine} cuisine contains {len(recipes)} recipes:")
        for recipe, ingredients in sorted(recipes.items(), key=lambda kvp: kvp[0]):
            result.append(f"  * {recipe} -> Ingredients: {', '.join(ingredients)}")

    return '\n'.join(result)


print(cookbook(
    ("Spaghetti Bolognese", "Italian", ["spaghetti", "tomato sauce", "ground beef"]),
    ("Margherita Pizza", "Italian", ["pizza dough", "tomato sauce", "mozzarella"]),
    ("Tiramisu", "Italian", ["ladyfingers", "mascarpone", "coffee"]),
    ("Croissant", "French", ["flour", "butter", "yeast"]),
    ("Ratatouille", "French", ["eggplant", "zucchini", "tomatoes"]),
    ("Sushi Rolls", "Japanese", ["rice", "nori", "fish", "vegetables"]),
    ("Miso Soup", "Japanese", ["tofu", "seaweed", "green onions"]),
    ("Guacamole", "Mexican", ["avocado", "tomato", "onion", "lime"])
))
