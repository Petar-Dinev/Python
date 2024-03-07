class Party:
    def __init__(self):
        self.people = []

    def add_people(self, name):
        self.people.append(name)

    def get_info(self):
        return f"Going: {', '.join(self.people)}\nTotal: {len(self.people)}"


party = Party()

while True:
    current_name = input()

    if current_name == 'End':
        break

    party.add_people(current_name)

print(party.get_info())
