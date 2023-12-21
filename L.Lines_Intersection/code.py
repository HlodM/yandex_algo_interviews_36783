from typing import List, Tuple


def get_intersection(first_sequence: List[Tuple[int, int]], second_sequence: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    i = j = 0
    intersection = []

    while i < len(first_sequence) and j < len(second_sequence):
        start_1, end_1 = first_sequence[i]
        start_2, end_2 = second_sequence[j]
        inter_start = max(start_1, start_2)
        if end_1 <= end_2:
            inter_end = end_1
            i += 1
        else:
            inter_end = end_2
            j += 1
        if inter_start <= inter_end:
            intersection.append((inter_start, inter_end))

    return intersection


def read_sequence() -> List[Tuple[int, int]]:
    n = int(input())
    sequnce = []
    for i in range(n):
        start, end = map(int, input().split())
        sequnce.append((start, end))
    return sequnce


def print_sequence(sequence: List[Tuple[int, int]]) -> None:
    for segment in sequence:
        print(segment[0], segment[1])


first_sequence = read_sequence()
second_sequence = read_sequence()
intersection = get_intersection(first_sequence, second_sequence)
print_sequence(intersection)
