from typing import List, Union, Dict

"""
Write a function how_sum(target_sum, numbers) that returns an array containing
any combination of elements that add up to exactly the target_sum. If there is
no combination that adds up o the target_sum. then return null.
"""


def how_sum(numbers: List[int], target_sum: int) -> Union[List[int], None]:
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    for num in numbers:
        remainder = target_sum - num
        combination = how_sum(numbers, remainder)
        if combination is not None:
            combination = combination + [num]
            return combination
    return None


def how_sum_memo(
    numbers: List[int], target_sum: int, memo: Dict[int, Union[List[int], None]]
) -> Union[List[int], None]:
    if target_sum == 0:
        return []
    if target_sum < 0:
        return None
    if target_sum in memo:
        return memo[target_sum]
    for num in numbers:
        remainder = target_sum - num
        combination = how_sum_memo(numbers, remainder, memo)
        if combination is not None:
            memo[target_sum] = combination + [num]
            return memo[target_sum]
    memo[target_sum] = None
    return memo[target_sum]


def how_sum_tabulation(numbers: List[int], target_sum: int) -> Union[List[int], None]:
    table_length = target_sum + 1
    table = [None] * table_length
    table[0] = []
    for i in range(table_length):
        if table[i] == [] or table[i] is not None:
            for number in numbers:
                forward = i + number
                if forward <= target_sum:
                    table[forward] = table[i] + [number]
    return table[target_sum]


if __name__ == "__main__":
    assert how_sum(numbers=[2, 3], target_sum=7) == [3, 2, 2]
    assert how_sum(numbers=[5, 3, 4, 7], target_sum=7) == [4, 3]
    assert not how_sum(numbers=[2, 4], target_sum=7)
    assert how_sum(numbers=[2, 3, 5], target_sum=8) == [2, 2, 2, 2]
    assert how_sum_memo(numbers=[2, 3], target_sum=7, memo={}) == [3, 2, 2]
    assert how_sum_memo(numbers=[5, 3, 4, 7], target_sum=7, memo={}) == [4, 3]
    assert not how_sum_memo(numbers=[2, 4], target_sum=7, memo={})
    assert how_sum_memo(numbers=[2, 3, 5], target_sum=8, memo={}) == [2, 2, 2, 2]
    assert not how_sum_memo(numbers=[7, 14], target_sum=300, memo={})
    assert how_sum_tabulation(numbers=[2, 3], target_sum=7) == [3, 2, 2]
    assert how_sum_tabulation(numbers=[5, 3, 4, 7], target_sum=7) == [4, 3]
    assert not how_sum_tabulation(numbers=[2, 4], target_sum=7)
    assert how_sum_tabulation(numbers=[2, 3, 5], target_sum=8) == [2, 2, 2, 2]
    assert not how_sum_tabulation(numbers=[7, 14], target_sum=300)
