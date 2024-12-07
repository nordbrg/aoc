import numpy as np

arrows = ["^", ">", "v", "<"]


def get_arrow_position():
    for i in arrows:
        c = np.argwhere(data == i)
        if c.size > 0:
            return c[0], i


def is_outside(c, data):
    if (
        c[0] - 1 < data.shape[0]
        and c[0] - 1 >= 0
        or c[0] + 1 < data.shape[0]
        and c[0] - 1 >= 0
        or c[1] - 1 < data.shape[1]
        and c[1] - 1 >= 0
        or c[1] + 1 < data.shape[1]
        and c[1] - 1 >= 0
    ):
        return True


def set_new_coordinate(c, arrow_dir):

    if arrow_dir == "^":
        if c[0] - 1 < data.shape[0] and c[0] - 1 >= 0:
            data[c[0] - 1, c[1]] = arrow_dir
        else:
            return True
    if arrow_dir == "v":
        if c[0] + 1 < data.shape[0] and c[0] - 1 >= 0:
            data[c[0] + 1, c[1]] = arrow_dir
        else:
            return True
    if arrow_dir == "<":
        if c[1] - 1 < data.shape[1] and c[1] - 1 >= 0:
            data[c[0], c[1] - 1] = arrow_dir
        else:
            return True
    if arrow_dir == ">":
        if c[1] + 1 < data.shape[1] and c[1] - 1 >= 0:
            data[c[0], c[1] + 1] = arrow_dir
        else:
            return True
    return False


def next_will_hit(c, arrow_dir):
    objects = np.argwhere(data == "#")
    will_collide = False

    if arrow_dir == "^":
        will_collide = any(
            np.array_equal(np.array([c[0] - 1, c[1]]), o) for o in objects
        )
    if arrow_dir == "v":
        will_collide = any(
            np.array_equal(np.array([c[0] + 1, c[1]]), o) for o in objects
        )
    if arrow_dir == "<":
        will_collide = any(
            np.array_equal(np.array([c[0], c[1] - 1]), o) for o in objects
        )
    if arrow_dir == ">":
        will_collide = any(
            np.array_equal(np.array([c[0], c[1] + 1]), o) for o in objects
        )
    return will_collide


def mark(c, t):
    data[c[0], c[1]] = t


def turn(arrow_dir):
    old_direction = arrows.index(arrow_dir)
    if old_direction == len(arrows) - 1:
        return arrows[0]
    return arrows[old_direction + 1]


def print_map():
    with open("f", "w") as f:
        for i in data:
            for j in i:
                f.write(str(j))
            f.write("\n")


def first_part():
    while 1:
        c, arrow_dir = get_arrow_position()
        hit = next_will_hit(c, arrow_dir)

        if hit:
            direction = turn(arrow_dir)
            mark(c, direction)
        else:
            mark(c, "x")
            outside = set_new_coordinate(c, arrow_dir)

            if outside:
                break

    print(len(np.argwhere(data == "x")))


def second_part():

    base, _ = get_arrow_position()

    def move(oy=-1, ox=-1):
        seen = set()
        y, x = base
        dy, dx = -1, 0
        while True:
            if y < 0 or y > data.shape[0] - 1 or x < 0 or x > data.shape[1] - 1:
                if oy == -1:
                    return len(seen)
                else:
                    return 0

            # turn
            if data[y][x] == "#" or (y == oy and x == ox):
                y -= dy
                x -= dx
                dy, dx = dx, -dy

            # already seen
            elif (y, x, dy, dx) in seen:
                return 1

            # handle seen
            else:
                if oy == -1:
                    seen.add((y, x))
                else:
                    seen.add((y, x, dy, dx))
                y += dy
                x += dx

    yp, xp = data.shape

    sum = sum(
        move(y, x)
        for y in range(yp)
        for x in range(xp)
        if data[y][x] != "#" or data[y][x] != "o"
    )

    print(sum)


with open("day6.dat", "r") as f:
    fdata = f.read()
    rows = [list(line) for line in fdata.strip().split("\n")]

data = np.array(rows)
first_part()

data = np.array(rows)
second_part()
