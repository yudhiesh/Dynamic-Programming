"""
You are a traveler on a 2D grid, you begin in the top-left corner and your goal
is to travel to the bottom-right corner. You can only move right or down. How
many ways can you travel to the goal on a grid with dimensions m * n
"""


from typing import Dict, List


def grid_traveler_recursive(row: int, col: int) -> int:
    if row == 1 and col == 1:
        return 1
    if row == 0 or col == 0:
        return 0
    return grid_traveler_recursive(row - 1, col) + grid_traveler_recursive(row, col - 1)


def grid_traveler_memo(row: int, col: int, memo: Dict[str, int]) -> int:
    if row == 1 and col == 1:
        return 1
    if row == 0 or col == 0:
        return 0
    key, key2 = f"{row},{col}", f"{col},{row}"
    if key in memo:
        return memo[key]
    if key2 in memo:
        return memo[key2]
    memo[key] = grid_traveler_memo(row - 1, col, memo) + grid_traveler_memo(
        row, col - 1, memo
    )
    return memo[key]


def grid_traveler_tabulation(row: int, col: int) -> int:
    table = [[0] * (col + 1) for _ in range(row + 1)]
    table[1][1] = 1
    for i in range(row + 1):
        for j in range(col + 1):
            current = table[i][j]
            if j + 1 <= col:
                table[i][j + 1] += current
            if i + 1 <= row:
                table[i + 1][j] += current

    return table[row][col]


if __name__ == "__main__":
    assert grid_traveler_recursive(1, 1) == 1
    assert grid_traveler_recursive(2, 3) == 3
    assert grid_traveler_recursive(3, 3) == 6
    assert grid_traveler_memo(3, 3, memo={}) == 6
    assert grid_traveler_memo(18, 18, memo={}) == 2333606220
    assert grid_traveler_tabulation(3, 3) == 6
    assert grid_traveler_tabulation(1, 1) == 1
    assert grid_traveler_tabulation(18, 18) == 2333606220
