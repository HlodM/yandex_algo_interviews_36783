from typing import List


def get_all_peaceful_combinations(n) -> List[List[int]]:
    all_ones = 2 ** n - 1
    bit_dict = {2**i: i+1 for i in range(n)}
    combinations = set()

    def place_queen(left_diag, column, right_diag, board, combinations, bit_dict=bit_dict, all_ones=all_ones):
        if column == all_ones:
            combinations.add(tuple(board))
            combinations.add(tuple(n+1-col for col in board))
            return
        possible_slots = ~(left_diag | column | right_diag) & all_ones
        while possible_slots:
            current_bit = possible_slots & -possible_slots
            possible_slots -= current_bit
            place_queen(
                (left_diag | current_bit) >> 1,
                column | current_bit,
                (right_diag | current_bit) << 1,
                board + [bit_dict[current_bit]],
                combinations
            )
            if not board and bit_dict[current_bit] == (n + 1) // 2 :
                break

    place_queen(0, 0, 0, [], combinations)
    return combinations


n = int(input())
combinations = get_all_peaceful_combinations(n)

print(len(combinations))
for combination in combinations:
    print(*combination)
