import collections
import itertools
import numpy as np


def solution(data):
    def _check_inside(p, data):
        return 0 <= p[0] < data.shape[0] and 0 <= p[1] < data.shape[1]

    antinodes = set()

    radar_positions = collections.defaultdict(set)
    [
        radar_positions[data[pos[0], pos[1]]].add((pos[0], pos[1]))
        for pos in np.argwhere(data != ".")
    ]

    for position in radar_positions.values():
        for (x0, y0), (x1, y1) in itertools.combinations(position, 2):
            if _check_inside((2 * x0 - x1, 2 * y0 - y1), data):
                antinodes.add((2 * x0 - x1, 2 * y0 - y1))

            if _check_inside((x1 - (x0 - x1), y1 - (y0 - y1)), data):
                antinodes.add((x1 - (x0 - x1), y1 - (y0 - y1)))

    print("1st part", len(antinodes))

    antinodes = set()

    for position in radar_positions.values():
        for (x0, y0), (x1, y1) in itertools.combinations(position, 2):
            p0, p1 = x0, y0
            while _check_inside((p0, p1), data):
                antinodes.add((p0, p1))
                p0 += x0 - x1
                p1 += y0 - y1

            p0, p1 = x1, y1
            while _check_inside((p0, p1), data):
                antinodes.add((p0, p1))
                p0 -= x0 - x1
                p1 -= y0 - y1

    print("2nd part", len(antinodes))


with open("day8.dat", "r") as f:
    fdata = f.read()
    rows = [list(line) for line in fdata.strip().split("\n")]


solution(np.array(rows))
