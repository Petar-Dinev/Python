letters = {
    'A': '.-',
    'B': '-...',
    "C": '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    "X": '-..-',
    'Y': '-.--',
    'Z': '--..'
}

current_input = input()
words = current_input.split(' | ')
message = ''

for word in words:
    characters = word.split()
    for char in characters:
        for letter, code in letters.items():
            if char == code:
                message += letter
    message += ' '

print(message.strip())
