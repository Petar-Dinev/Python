class Stack:
    def __init__(self):
        self.data: list = []

    def push(self, element: str) -> None:
        self.data.append(element)

    def pop(self) -> str:
        return self.data.pop()

    def top(self):
        el = self.data[-1]
        return el

    def is_empty(self) -> bool:
        if self.data:
            return False
        return True

    def __str__(self):
        return f"[{', '.join(self.data[::-1])}]"
