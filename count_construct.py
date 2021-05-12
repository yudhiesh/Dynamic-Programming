"""
Write a function count_construct that accepts a target string and an array of
strings. The function should return the number of ways that can be done to
generate the target string
"""

from typing import Dict, List


def count_construct_recursive(target: str, word_bank: List[str]) -> int:
    if target == "":
        return 1
    count = 0
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word) :]
            count += count_construct_recursive(suffix, word_bank)
    return count


def count_construct_memo(
    target: str, word_bank: List[str], memo: Dict[str, int]
) -> int:
    if target in memo:
        return memo[target]
    if target == "":
        return 1
    count = 0
    for word in word_bank:
        if target.startswith(word):
            suffix = target[len(word) :]
            count += count_construct_memo(suffix, word_bank, memo)
    memo[target] = count
    return memo[target]


def count_construct_tabulation(target: str, word_bank: List[str]) -> int:
    target_length = len(target)
    table_length = target_length + 1
    table = [0] * table_length
    table[0] = 1
    count = 0
    for i in range(table_length):
        if table[i] > 0:
            for word in word_bank:
                forward = i + len(word)
                if target[:forward].startswith(word) and forward <= table_length:
                    count += 1
    return table[target_length]


if __name__ == "__main__":
    LONG_E = "e" * 39
    assert (
        count_construct_recursive(
            target="purple", word_bank=["purp", "p", "ur", "le", "purpl"]
        )
        == 2
    )
    assert (
        count_construct_recursive(
            target="abcdef", word_bank=["ab", "abc", "cd", "def", "abcd"]
        )
        == 1
    )
    assert (
        count_construct_recursive(
            target="skateboard", word_bank=["bo", "rd", "ate", "t", "ska", "sk", "boar"]
        )
        == 0
    )
    assert (
        count_construct_recursive(
            target="enterapotentpot",
            word_bank=["a", "p", "ent", "enter", "ot", "o", "t"],
        )
        == 4
    )
    # WAYY TOO SLOW
    # assert (
    #     count_construct_recursive(
    #         target=f"{LONG_E}f", word_bank=["e" * i for i in range(1, 7)]
    #     )
    #     == 0
    # )
    assert (
        count_construct_memo(
            target="purple", word_bank=["purp", "p", "ur", "le", "purpl"], memo={}
        )
        == 2
    )
    assert (
        count_construct_memo(
            target="abcdef", word_bank=["ab", "abc", "cd", "def", "abcd"], memo={}
        )
        == 1
    )
    assert (
        count_construct_memo(
            target="skateboard",
            word_bank=["bo", "rd", "ate", "t", "ska", "sk", "boar"],
            memo={},
        )
        == 0
    )
    assert (
        count_construct_memo(
            target="enterapotentpot",
            word_bank=["a", "p", "ent", "enter", "ot", "o", "t"],
            memo={},
        )
        == 4
    )
    assert (
        count_construct_memo(
            target=f"{LONG_E}f", word_bank=["e" * i for i in range(1, 7)], memo={}
        )
        == 0
    )
    assert (
        count_construct_tabulation(
            target="purple", word_bank=["purp", "p", "ur", "le", "purpl"]
        )
        == 2
    )
    assert (
        count_construct_tabulation(
            target="abcdef", word_bank=["ab", "abc", "cd", "def", "abcd"]
        )
        == 1
    )
    assert (
        count_construct_tabulation(
            target="skateboard", word_bank=["bo", "rd", "ate", "t", "ska", "sk", "boar"]
        )
        == 0
    )
    assert (
        count_construct_tabulation(
            target="enterapotentpot",
            word_bank=["a", "p", "ent", "enter", "ot", "o", "t"],
        )
        == 4
    )
    assert (
        count_construct_tabulation(
            target=f"{LONG_E}f", word_bank=["e" * i for i in range(1, 7)]
        )
        == 0
    )
