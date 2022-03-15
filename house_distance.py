# ID 64131430
from typing import List

def find_distances(houses, empty_house='0') -> List[int]:
    number_of_houses = len(houses)
    result = [0] * number_of_houses
    zeros = [index for index, house in enumerate(houses) if house == empty_house]
    first_zero = zeros[0]
    for index in range(0, first_zero):
        result[index] = (first_zero - index)
    for previous, current in zip(zeros, zeros[1:]):
        for index in range(previous + 1, current):
            result[index] = min(
                index - previous,
                current - index     
            )
    last_zero = zeros[-1]
    for index in range(last_zero + 1, number_of_houses):
        result[index] = index - last_zero
    return result


if __name__ == '__main__':
    input()
    print(*find_distances(input().split()))
