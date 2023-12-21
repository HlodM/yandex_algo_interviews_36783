from typing import List


def get_max_xor(numbers: List[int]) -> int:
    max_xor = 0
    for bit_pos in range(31, -1, -1):
        max_xor <<= 1
        prefixes = {num >> bit_pos for num in numbers}
        for prefix in prefixes:
            if (max_xor + 1) ^ prefix in prefixes:
                max_xor += 1
                break
    return max_xor


n = int(input())
numbers = list(map(int, input().split()))
print(get_max_xor(numbers))
