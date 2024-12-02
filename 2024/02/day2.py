import numpy as np

is_sorted_dec = lambda a: np.all(a[:-1] >= a[1:])
is_sorted_asc = lambda a: np.all(a[:-1] <= a[1:])


def first_part():
    result = 0

    with open("day2.dat") as f:
        for line in f:
            data = np.fromstring(line.strip(), dtype=int, sep=" ")

            diff_max = abs(np.diff(data)).max()
            diff_min = abs(np.diff(data)).min()

            if is_sorted_dec(data) or is_sorted_asc(data):
                if diff_min > 0 and diff_max <= 3:
                    result = result + 1

    print(result)


def second_part():
    with open("day2.dat") as f:
        for line in f:
            data = np.fromstring(line.strip(), dtype=int, sep=" ")

            for i in range(len(data)):
                data = data[:i] + data[1 + i :]

                diff_max = abs(np.diff(data)).max()
                diff_min = abs(np.diff(data)).min()

                if is_sorted_dec(data) or is_sorted_asc(data):
                    if diff_min > 0 and diff_max <= 3:
                        result = result + 1
    print(result)

first_part()
second_part()
