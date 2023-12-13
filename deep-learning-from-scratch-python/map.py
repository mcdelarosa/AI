import random


def generate_random_row():
    probability = random.random()  # Generate a random number between 0 and 1

    if probability <= 0.25:
        # 25% of the time, all values are zero
        return [0, 0, 0]
    elif 0.25 < probability <= 0.5:
        # 25% of the time, two values are 1 in random positions
        two_ones = [0, 0, 0]
        positions = random.sample([0, 1, 2], 2)
        for pos in positions:
            two_ones[pos] = 1
        return two_ones
    else:
        # Default case: 50% of the time, one value is 1 in a random position
        one_one = [0, 0, 0]
        one_position = random.randint(0, 2)
        one_one[one_position] = 1
        return one_one

def generate_random_list(row_number):
    new_list = []
    for _ in range(row_number):
        probability = random.random()  # Generate a random number between 0 and 1

        if probability <= 0.25:
            # 25% of the time, all values are zero
            new_list.append([0, 0, 0])
        elif 0.25 < probability <= 0.5:
            # 25% of the time, two values are 1 in random positions
            two_ones = [0, 0, 0]
            positions = random.sample([0, 1, 2], 2) # chooses the two positions to put 1
            for pos in positions:
                two_ones[pos] = 1
            new_list.append(two_ones)
        else:
            # Default case: 50% of the time, one value is 1 in a random position
            one_one = [0, 0, 0]
            one_position = random.randint(0, 2)
            one_one[one_position] = 1
            new_list.append(one_one)

    return new_list

result = generate_random_list(15)
for row in result:
    print(",".join(map(str, row)))
