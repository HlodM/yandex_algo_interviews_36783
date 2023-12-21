from typing import List


def dfs(matrix: List[List[int]], matrix_of_paths, row, col, n, m):
    deltas = tuple(((-1, 0), (1, 0), (0, -1), (0, 1)))
    stack = [[row, col]]
    while stack:
        cur_row, cur_col = stack[-1]
        cur_path = 1
        flag = True
        for dx, dy in deltas:
            if 0 <= cur_row + dx < n and 0 <= cur_col + dy < m:
                if matrix[cur_row][cur_col] < matrix[cur_row + dx][cur_col + dy]:
                    if not matrix_of_paths[cur_row + dx][cur_col + dy]:
                        stack.append([cur_row + dx, cur_col + dy])
                        flag = False
                        break
                    cur_path = max(cur_path, matrix_of_paths[cur_row + dx][cur_col + dy] + 1)
        if flag:
            matrix_of_paths[cur_row][cur_col] = cur_path
            stack.pop()


def get_longest_increasing_path(matrix: List[List[int]], n: int, m: int) -> int:
    matrix_of_paths = [[0] * m for _ in range(n)]
    longest_path = 0
    for row in range(n):
        for col in range(m):
            if not matrix_of_paths[row][col]:
                dfs(matrix, matrix_of_paths, row, col, n, m)
            longest_path = max(longest_path, matrix_of_paths[row][col])

    return longest_path


with open('input.txt') as f:
    n, m = map(int, f.readline().split())
    matrix = []
    for i in range(n):
        matrix.append(list(map(int, f.readline().split())))


print(get_longest_increasing_path(matrix, n, m))
