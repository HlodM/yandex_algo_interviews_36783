from typing import List, Tuple


def is_on_one_line(points: List[Tuple[int]]) -> bool:
    x_start, y_start = points[0]
    slope = None

    for point in points[1:]:
        if point == points[0]:
            continue
        else:
            x_cur, y_cur = point
            slope_cur = (y_cur - y_start), (x_cur - x_start)
            if not slope:
                slope = slope_cur
            elif slope[1] * slope_cur[0] != slope_cur[1] * slope[0]:
                return False
    return True


n = int(input())
points = []
for i in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

if is_on_one_line(points):
    print('YES')
else:
    print('NO')
