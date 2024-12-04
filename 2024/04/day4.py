import numpy as np

# https://numpy.org/doc/stable/reference/generated/numpy.all.html ~ like any()
# https://numpy.org/doc/stable/reference/generated/numpy.lib.stride_tricks.sliding_window_view.html ~ check pattern in the moving window
# https://numpy.org/doc/stable/reference/generated/numpy.logical_or.html#numpy-logical-or ~ for matching


def get_data(pattern):
    return np.array(list(map(list, pattern)))


def matches(m):
    return np.sum(
        np.all(
            np.logical_or(
                np.lib.stride_tricks.sliding_window_view(data, m.shape) == m,
                m == "-",
            ),
            axis=(2, 3),
        )
    )


def first_part():
    h_and_v = sum(
        matches(np.rot90(get_data(pattern=word), i)) for i in range(len(word))
    )
    pattern = ("X---", "-M--", "--A-", "---S")
    diag = sum(
        matches(np.rot90(get_data(pattern=pattern), i)) for i in range(len(word))
    )
    print(h_and_v + diag)


def second_part():
    pattern = ("M-S", "-A-", "M-S")
    print(
        sum(matches(np.rot90(get_data(pattern=pattern), i)) for i in range(len(word)))
    )


word = "XMAS"
data = get_data(open("day4.dat").read().splitlines())

first_part()
second_part()
