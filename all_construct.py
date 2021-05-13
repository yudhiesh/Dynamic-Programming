"""
Write a function that accepts a target string an an array of strings. The
function should return a 2D array containing all of the ways that the target cna
be constructed by concatenating elements of the wordBank array.
"""

from typing import Dict, List


def all_construct_recursive(target: str, word_bank: List[str]) -> List[List[str]]:
    if target == "":
        return [[]]
    result = []
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word) :]
            suffix_ways = all_construct_recursive(suffix, word_bank)
            target_ways = [way + [word] for way in suffix_ways]
            if target_ways:
                result.extend(target_ways)
    return result


def all_construct_memo(
    target: str, word_bank: List[str], memo: Dict
) -> List[List[str]]:
    if target in memo:
        return memo[target]
    if target == "":
        return [[]]
    result = []
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word) :]
            suffix_ways = all_construct_memo(suffix, word_bank, memo)
            target_ways = [way + [word] for way in suffix_ways]
            if target_ways:
                result.extend(target_ways)
    memo[target] = result
    return result


def all_construct_tabulation(target: str, word_bank: List[str]) -> List[List[str]]:
    table = [[] for _ in range(len(target) + 1)]
    table[0] = [[]]
    for i in range(len(target)):
        for word in word_bank:
            if target[i : i + len(word)] == word:
                new_combinations = [combination + [word] for combination in table[i]]
                table[i + len(word)].extend(new_combinations)
    return table[-1]


if __name__ == "__main__":
    assert (
        all_construct_recursive(
            target="purple", word_bank=["purp", "p", "ur", "le", "purpl"]
        )
    ) == [["le", "purp"], ["le", "p", "ur", "p"]]
    assert (
        all_construct_memo(
            target="purple", word_bank=["purp", "p", "ur", "le", "purpl"], memo={}
        )
    ) == [["le", "purp"], ["le", "p", "ur", "p"]]
    assert (
        all_construct_tabulation(
            target="purple", word_bank=["purp", "p", "ur", "le", "purpl"]
        )
    ) == [['purp', 'le'], ['p', 'ur', 'p', 'le']]
