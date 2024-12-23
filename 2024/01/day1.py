def get_data(data):
    left = []
    right = []

    with open(data, "r") as f:
        for l in f:
            k = l.replace("\n", "").split("   ")
            left.append(k[0])
            right.append(k[1])
    return left, right


def first_part():
    distance = 0

    left, right = get_data("day1.dat")

    left = sorted(left)
    right = sorted(right)

    for i in range(0, len(left)):
        distance = distance + abs(int(left[i]) - int(right[i]))

    print(f"Distance: {distance}")


def second_part():
    similarity_score = 0

    left, right = get_data("day1.dat")

    for i in range(0, len(left)):
        act_sim_score = right.count(left[i])
        similarity_score = similarity_score + (int(left[i]) * act_sim_score)

    print(f"Similarity score: {similarity_score}")


first_part()
second_part()
