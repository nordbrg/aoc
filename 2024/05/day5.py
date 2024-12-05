import numpy as np

with open("day5.dat", "r") as f:
    data = f.read()

rules = np.array([i.split("|") for i in data.split("\n\n")[0].split("\n")], dtype=int)
pages = data.split("\n\n")[1].split("\n")


def first_part():
    sum = 0

    for page in pages:
        page = np.fromstring(page, sep=",", dtype=int)
        nr_of_rules = len(page) - 1

        for j in range(nr_of_rules):
            pair = np.array([page[j], page[j + 1]])
            is_present = any(np.array_equal(pair, rule) for rule in rules)
            nr_of_rules -= 1 if is_present else 0

        sum += page[len(page) // 2] if nr_of_rules == 0 else 0

    print(f"First: ", sum)
    return sum


def second_part(first_sum):
    sum = 0

    for page in pages:
        page = np.fromstring(page, sep=",", dtype=int)
        nr_of_rules = len(page) - 1

        def fix():
            for j in range(nr_of_rules):
                pair = np.array([page[j], page[j + 1]])

                is_present = any(np.array_equal(pair, rule) for rule in rules)
                if is_present:
                    continue

                pair = np.flip(pair)
                page[j : j + 2] = pair
                fix()

        fix()
        sum += page[len(page) // 2]

    print(f"Second: ", sum - first_sum)


sum = first_part()
second_part(sum)
