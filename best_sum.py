from typing import Dict, List, Optional, Union

"""
Write a function best_sum which returns an array containing the shortest
combination of numbers that add up to exactly the target_sum.
If there is a tie for any of the shortest combinations then you may return any
of them.
"""


def best_sum(numbers: List[int], target_sum: int) -> Optional[List[int]]:
    shortest_combination = None
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    for number in numbers:
        remainder = target_sum - number
        remainder_combination = best_sum(numbers, remainder)
        if remainder_combination is not None:
            combination = remainder_combination + [number]
            if shortest_combination is None or len(combination) < len(
                shortest_combination
            ):
                shortest_combination = combination
    return shortest_combination


def best_sum_memo(
    numbers: List[int], target_sum: int, memo: Dict[int, Optional[List[int]]]
) -> Optional[Union[List[int], Optional[int]]]:
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    if target_sum in memo:
        return memo[target_sum]
    shortest_combination = None
    for number in numbers:
        remainder = target_sum - number
        remainder_combination = best_sum_memo(numbers, remainder, memo)
        if remainder_combination is not None:
            combination = remainder_combination + [number]  # type: ignore
            if shortest_combination is None or len(combination) < len(
                shortest_combination
            ):
                shortest_combination = combination
    memo[target_sum] = shortest_combination
    return shortest_combination


def best_sum_tabulation(
    numbers: List[int], target_sum: int
) -> Optional[Union[List[int], Optional[int]]]:
    table_length = target_sum + 1
    table = [None for _ in range(table_length)]
    table[0] = []  # type: ignore
    for i in range(table_length):
        if table[i] == [] or table[i]:
            for number in numbers:
                forward = i + number
                forward_value = table[i] + [number]  # type: ignore
                if forward <= target_sum:
                    if table[forward] is None:
                        table[forward] = forward_value
                    table[forward] = min(forward_value, table[forward], key=len)  # type: ignore
    return table[target_sum]


if __name__ == "__main__":
    assert best_sum([5, 3, 4, 7], 7) == [7]
    assert best_sum([2, 3, 5], 8) == [3, 5] or [5, 3]
    assert best_sum([1, 4, 5], 8) == [4, 4]
    assert best_sum_memo([5, 3, 4, 7], 7, {}) == [7]
    assert best_sum_memo([2, 3, 5], 8, {}) == [3, 5] or [5, 3]
    assert best_sum_memo([1, 4, 5], 8, {}) == [4, 4]
    assert best_sum_memo([1, 2, 5, 25], 100, {}) == [25, 25, 25, 25]
    assert best_sum_tabulation([5, 3, 4, 7], 7) == [7]
    assert best_sum_tabulation([2, 3, 5], 8) == [3, 5] or [5, 3]
    assert best_sum_tabulation([1, 4, 5], 8) == [4, 4]
    assert best_sum_tabulation([1, 2, 5, 25], 100) == [25, 25, 25, 25]
