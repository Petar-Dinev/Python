tickets = input().split(', ')
winning_symbols = ['@', '#', '$', '^']

for ticket in tickets:
    ticket = ticket.strip()

    if len(ticket) == 20:
        first_half = ticket[:10]
        second_half = ticket[10:]
        is_winning = False
        winning_symbol_is = ''
        winning_length = 0
        for symbol in winning_symbols:
            for i in range(10, 5, -1):
                if symbol * i in first_half and symbol * i in second_half:
                    is_winning = True
                    winning_symbol_is = symbol
                    winning_length = i
                    break
        if is_winning:
            if winning_length == 10:
                print(f'ticket "{ticket}" - {winning_length}{winning_symbol_is} Jackpot!')
            else:
                print(f'ticket "{ticket}" - {winning_length}{winning_symbol_is}')
        else:
            print(f'ticket "{ticket}" - no match')
    else:
        print('invalid ticket')
