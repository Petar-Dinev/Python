from typing import List


class Smartphone:

    def __init__(self, memory: float):
        self.memory = memory
        self.apps: List[str] = []
        self.is_on: bool = False

    def power(self) -> None:
        self.is_on = not self.is_on

    def install(self, app: str, app_memory: float) -> str:
        if self.is_on and app_memory <= self.memory:
            self.memory -= app_memory
            self.apps.append(app)
            return f"Installing {app}"

        if not self.is_on and app_memory <= self.memory:
            return f"Turn on your phone to install {app}"

        return f"Not enough memory to install {app}"

    def status(self) -> str:
        return f"Total apps: {len(self.apps)}. Memory left: {self.memory}"


# test code:
smartphone = Smartphone(100)
print(smartphone.install("Facebook", 60))
smartphone.power()
print(smartphone.install("Facebook", 60))
print(smartphone.install("Messenger", 20))
print(smartphone.install("Instagram", 40))
print(smartphone.status())
