contestants = [int(num) for num in input().split()]
pies = [int(num) for num in input().split()]
message = ''

while True:
    current_contestant = contestants[0]
    current_pie_to_eat = pies[-1]
    if current_contestant >= current_pie_to_eat:
        current_contestant = contestants.pop(0)
        current_contestant -= current_pie_to_eat
        pies.pop(-1)
        if current_contestant > 0:
            contestants.append(current_contestant)
    else:
        pies[-1] -= current_contestant
        contestants.pop(0)
        if pies[-1] == 1 and len(pies) > 1:
            pies.pop(-1)
            pies[-1] += 1

    if len(pies) == 0 and len(contestants) > 0:
        message = "We will have to wait for more pies to be baked!"
    elif len(contestants) == 0 and len(pies) > 0:
        message = "Our contestants need to rest!"
    elif len(pies) == 0 and len(contestants) == 0:
        message = "We have a champion!"
    if len(pies) == 0 or len(contestants) == 0:
        break

print(message)
if len(pies) > 0:
    pies = map(str, pies)
    print(f"Pies left: {', '.join(pies)}")
if len(contestants) > 0:
    contestants = list(map(str, contestants))
    print(f"Contestants left: {', '.join(contestants)}")
