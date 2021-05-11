from typing import List

"""
Write a function canSum(numbers, target_sum)  that returns a boolean indicating
whether or not it is possible to generate the target using numbers in the array
"""


def can_sum(array: List[int], target: int) -> bool:
    if target == 0:
        return True
    if target < 0:
        return False
    elements = {}
    for idx, a in enumerate(array):
        remaining = target - a
        if remaining in elements:
            return True
        elements[a] = idx
    return False


def can_sum_tabulation(numbers: List[int], target: int) -> bool:
    table = [False] * (target + 1)
    table[0] = True
    for i in range(target + 1):
        if table[i]:
            for num in numbers:
                forward = i + num
                if forward <= target:
                    table[forward] = True
    return table[target]


if __name__ == "__main__":
    assert can_sum(array=[5, 3, 4, 7], target=7)
    assert can_sum(array=[5, 3, 4, 7], target=0)
    assert can_sum_tabulation(numbers=[2, 3], target=7)
    assert can_sum_tabulation(numbers=[5, 3, 4, 7], target=0)
    assert not can_sum_tabulation(numbers=[2, 4], target=7)
    assert can_sum_tabulation(numbers=[2, 3, 5], target=8)
    assert not can_sum_tabulation(numbers=[7, 14], target=300)
