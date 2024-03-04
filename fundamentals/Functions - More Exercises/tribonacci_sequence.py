def make_tribonacci_sequence(num):
    result = [1]
    while len(result) < num:
        current_sum = sum(result[-3:])
        result.append(current_sum)
    print(*result, sep=' ')


num_input = int(input())
make_tribonacci_sequence(num_input)
