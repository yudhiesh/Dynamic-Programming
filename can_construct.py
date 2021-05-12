"""
Write a function can_construct that accepts a target string and an array of
strings. The function should return a boolean indicating whether or not the
target can be constructed by concatenating elements of the wordBank array. You
may reuse elements of wordBank as many times as needed.
"""

from typing import Dict, List


def can_construct_recursive(target: str, word_bank: List[str]) -> bool:
    if target == "":
        return True

    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word) :]
            if can_construct_recursive(suffix, word_bank):
                return True
    return False


def can_construct_memo(target: str, word_bank: List[str], memo=Dict[str, bool]) -> bool:
    if target in memo:
        return memo[target]
    if target == "":
        return True
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word) :]
            if can_construct_memo(suffix, word_bank, memo):
                memo[target] = True
                return memo[target]
    memo[target] = False
    return False


def can_construct_tabulation(target: str, word_bank: List[str]) -> bool:
    target_length = len(target)
    table_length = target_length + 1
    table = [False for _ in range(table_length)]
    table[0] = True  # type: ignore
    for i in range(target_length):
        if table[i]:
            for word in word_bank:
                forward = len(word) + i
                if target[i: forward].startswith(word):
                    if forward < table_length:
                        table[forward] = True  # type: ignore
    return table[target_length]


if __name__ == "__main__":
    LONG_E = "e" * 39
    assert can_construct_recursive(
        target="abcdef", word_bank=["ab", "abc", "cd", "def", "abcd"]
    )
    assert not can_construct_recursive(
        target="skateboard", word_bank=["bo", "rd", "ate", "t", "ska", "sk", "boar"]
    )
    assert can_construct_recursive(
        target="enterapotentpot", word_bank=["a", "p", "ent", "enter", "ot", "o", "t"]
    )
    assert can_construct_memo(
        target="enterapotentpot",
        word_bank=["a", "p", "ent", "enter", "ot", "o", "t"],
        memo={},
    )
    assert not can_construct_memo(
        target=f"{LONG_E}f", word_bank=["e" * i for i in range(1, 7)], memo={}
    )
    assert can_construct_tabulation(
        target="abcdef", word_bank=["ab", "abc", "cd", "def", "abcd"]
    )
    assert not can_construct_tabulation(
        target="skateboard", word_bank=["bo", "rd", "ate", "t", "ska", "sk", "boar"]
    )
    assert can_construct_tabulation(
        target="enterapotentpot", word_bank=["a", "p", "ent", "enter", "ot", "o", "t"]
    )
    assert can_construct_tabulation(
        target="enterapotentpot",
        word_bank=["a", "p", "ent", "enter", "ot", "o", "t"],
    )
    assert not can_construct_tabulation(
        target=f"{LONG_E}f", word_bank=["e" * i for i in range(1, 7)]
    )
