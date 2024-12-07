def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def concatenate(a, b):
    return int(str(a) + str(b))


def calculator(pos, values, do):
    if len(values) == 0:
        return [pos]

    r = []
    for d in do:
        r.append(calculator(d(pos, values[0]), values[1:], do))

    return sum(r, [])


def first_part(to_solve):
    sum = 0
    do = [add, multiply]
    for result, values in to_solve:
        calculated = calculator(values[0], values[1:], do)
        if result in calculated:
            sum += result
    print(sum)


def second_part(to_solve):
    sum = 0
    calculated = []
    do = [add, multiply, concatenate]
    for result, values in to_solve:
        calculated = calculator(values[0], values[1:], do)
        if result in calculated:
            sum += result
    print(sum)


data = []
to_solve = []

with open("day7.dat", "r") as f:
    for l in f.readlines():
        data.append(l.strip().split(": "))

for i, j in data:
    l = list(map(int, j.split(" ")))
    to_solve.append([int(i), l])

first_part(to_solve)
second_part(to_solve)
