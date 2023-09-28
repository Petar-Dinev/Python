budget = float(input())
num_of_video_cards = int(input())
num_of_processors = int(input())
num_of_ram_memories = int(input())

video_card_price = 250

total_cost_for_video_cards = num_of_video_cards * video_card_price
total_cost_for_processors = num_of_processors * total_cost_for_video_cards * 0.35
total_cost_for_ram_memories = num_of_ram_memories * total_cost_for_video_cards * 0.1
total_cost = total_cost_for_video_cards + total_cost_for_processors + total_cost_for_ram_memories

if num_of_video_cards > num_of_processors:
    total_cost *= 0.85

difference = abs(total_cost - budget)
if budget >= total_cost:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")
