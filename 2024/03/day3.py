import re


def first_part():
    with open("day3.dat", "r") as f:
        data = f.read()
        pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
        matches = re.findall(pattern, data)
        results = sum([int(a) * int(b) for a, b in matches])

        print(results)


def second_part():
    with open("day3.dat", "r") as f:
        data = f.read()
        pattern = r"(do\(\)|don\'t\(\)|mul\((\d{1,3}),(\d{1,3})\))"
        matches = re.findall(pattern, data)

        sum = 0
        active = True
        for a, b, c in matches:
            if a == "don't()":
                active = False
            if a == "do()":
                active = True
            if b and c != "" and active:
                sum = sum + (int(b) * int(c))
        print(sum)

first_part()
second_part()
