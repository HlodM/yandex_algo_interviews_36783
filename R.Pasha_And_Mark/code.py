def is_pasha_wins(n: int) -> bool:
    return n % 2 == 0


n = int(input())
if is_pasha_wins(n):
    print('Pasha')
else:
    print('Mark')
