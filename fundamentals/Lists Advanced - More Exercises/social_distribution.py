population = [int(num) for num in input().split(', ')]
min_wealth = int(input())

can_equal_distribute = False

if sum(population) / len(population) >= min_wealth:
    can_equal_distribute = True

if can_equal_distribute:
    for i in range(len(population)):
        if population[i] < min_wealth:
            biggest_num = 0
            for num in population:
                if num > biggest_num:
                    biggest_num = num
            different = min_wealth - population[i]
            if biggest_num - different >= min_wealth:
                population[i] += different
                index = population.index(biggest_num)
                population[index] -= different
    print(population)
else:
    print("No equal distribution possible")
