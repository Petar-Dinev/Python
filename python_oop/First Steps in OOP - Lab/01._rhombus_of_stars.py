size = int(input())


def print_first_part_of_rhombus(size_):
    for i in range(1, size + 1):
        print(f"{' ' * (size_ - i)}{'* ' * i}")


def print_second_part_of_rhombus(size__):
    for i in range(size__ - 1, 0, -1):
        print(f"{' ' * (size__ - i)}{'* ' * i}")


def main(size_of_rhombus):
    print_first_part_of_rhombus(size_of_rhombus)
    print_second_part_of_rhombus(size_of_rhombus)


main(size)
