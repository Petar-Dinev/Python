cards_list = input().split()
shuffle_count = int(input())
half_cards_length = len(cards_list) // 2

for _ in range(shuffle_count):
    current_deck = []
    for i in range(half_cards_length):
        first_half_of_cards = cards_list[:half_cards_length]
        second_half_of_cards = cards_list[half_cards_length:]
        current_deck.append(first_half_of_cards[i])
        current_deck.append(second_half_of_cards[i])
    cards_list = current_deck

print(cards_list)
