def get_number_of_good_pairs(numbers) -> int:
    remainder_list = [[0, 0] for _ in range(200)]
    for num in numbers:
        idx = num % 200
        remainder_list[idx][0] += remainder_list[idx][1]
        remainder_list[idx][1] += 1
    return sum(el[0] for el in remainder_list)


n = int(input())
numbers = list(map(int, input().split()))
print(get_number_of_good_pairs(numbers))
