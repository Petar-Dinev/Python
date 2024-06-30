from typing import List
from project.pokemon import Pokemon


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons: List[Pokemon] = []

    def add_pokemon(self, pokemon_: Pokemon) -> str:
        if pokemon_ not in self.pokemons:
            self.pokemons.append(pokemon_)
            return f"Caught {pokemon_.pokemon_details()}"

        return "This pokemon is already caught"

    def release_pokemon(self, pokemon_name: str) -> str:
        search_pokemon_list = [p for p in self.pokemons if p.name == pokemon_name]
        if search_pokemon_list:
            self.pokemons.remove(search_pokemon_list[0])
            return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self) -> str:
        result = [f"Pokemon Trainer {self.name}", f"Pokemon count {len(self.pokemons)}"]
        for pokemon_ in self.pokemons:
            result.append(f"- {pokemon_.pokemon_details()}")
        return '\n'.join(result)


# test code:
pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
