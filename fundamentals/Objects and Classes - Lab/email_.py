class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
send_indices = []

while True:
    current_input = input()

    if current_input == 'Stop':
        break

    sender_, receiver_, content_ = current_input.split()
    email = Email(sender_, receiver_, content_)
    emails.append(email)

indices = input().split(', ')

for i in indices:
    current_email = emails[int(i)]
    current_email.send()

for email_ in emails:
    print(email_.get_info())
