from typing import List

from project.animal import Animal
from project.worker import Worker


class Zoo:

    def __init__(self, name: str, budget: int, animal_capacity: int, workers_capacity: int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals: List[Animal] = []
        self.workers: List[Worker] = []

    def add_animal(self, animal: Animal, price: float):
        if self.__animal_capacity == len(self.animals):
            return "Not enough space for animal"

        if self.__animal_capacity > len(self.animals) and price > self.__budget:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price
        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity == len(self.workers):
            return "Not enough space for worker"

        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name: str):
        worker = next((w for w in self.workers if w.name == worker_name), None)
        if worker:
            self.workers.remove(worker)
            return f"{worker_name} fired successfully"
        else:
            return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries = sum([w.salary for w in self.workers])
        if self.__budget >= salaries:
            self.__budget -= salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        else:
            return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        need_money = sum([a.money_for_care for a in self.animals])
        if self.__budget >= need_money:
            self.__budget -= need_money
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        else:
            return f"You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = [f"You have {len(self.animals)} animals"]
        lions = [a for a in self.animals if a.__class__.__name__ == 'Lion']
        tigers = [a for a in self.animals if a.__class__.__name__ == 'Tiger']
        cheetahs = [a for a in self.animals if a.__class__.__name__ == 'Cheetah']
        result.append(f"----- {len(lions)} Lions:")
        for lion in lions:
            result.append(lion.__repr__())
        result.append(f"----- {len(tigers)} Tigers:")
        for tiger in tigers:
            result.append(tiger.__repr__())
        result.append(f"----- {len(cheetahs)} Cheetahs:")
        for cheetah in cheetahs:
            result.append(cheetah.__repr__())

        return '\n'.join(result)

    def workers_status(self):
        result = [f"You have {len(self.workers)} workers"]
        keepers = [w for w in self.workers if w.__class__.__name__ == 'Keeper']
        result.append(f"----- {len(keepers)} Keepers:")
        for keeper in keepers:
            result.append(keeper.__repr__())
        caretakers = [w for w in self.workers if w.__class__.__name__ == 'Caretaker']
        result.append(f"----- {len(caretakers)} Caretakers:")
        for caretaker in caretakers:
            result.append(caretaker.__repr__())
        vets = [w for w in self.workers if w.__class__.__name__ == 'Vet']
        result.append(f"----- {len(vets)} Vets:")
        for vet in vets:
            result.append(vet.__repr__())

        return '\n'.join(result)
