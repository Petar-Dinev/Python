class Zoo:
    def __init__(self, name_of_zoo):
        self.name_of_zoo = name_of_zoo
        self.__animals = 0
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        self.__animals += 1
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)

    def get_info(self, species):
        current_species_list = []
        if species == 'mammal':
            species = 'Mammals'
            current_species_list = self.mammals
        elif species == 'fish':
            species = 'Fishes'
            current_species_list = self.fishes
        elif species == 'bird':
            species = 'Birds'
            current_species_list = self.birds
        return f"{species} in {self.name_of_zoo}: {', '.join(current_species_list)}\nTotal animals: {self.__animals}"


name_of_zoo_ = input()
zoo = Zoo(name_of_zoo_)
num_of_animals = int(input())

for i in range(num_of_animals):
    species_of_animal, name_of_animal = input().split()
    zoo.add_animal(species_of_animal, name_of_animal)

search_species = input()
print(zoo.get_info(search_species))
