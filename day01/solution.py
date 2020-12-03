import itertools
import math

magic_number = 2020

def check_sum(some_list, magic_number=magic_number):
    int_list = [int(i) for i in some_list]
    addition = sum(int_list)
    if addition == magic_number:
        product = math.prod(int_list)
        print("Numbers were: ", int_list)
        print("Their product is: ", product)


with open("./input.txt") as f:
    items = f.read().splitlines()
    # combinations(range(4), 3) --> 012 013 023 123
    # Part 1
    for a, b in itertools.combinations(items, 2):
        check_sum([a, b])

    # Part 2
    for a, b, c in itertools.combinations(items, 3):
        check_sum([a, b, c])
