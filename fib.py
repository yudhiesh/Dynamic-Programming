"""
Given a value N find the fibonacci number at that position
"""


def fib_recursive(n: int) -> int:
    cache = {}
    if n == 0:
        return 0
    if 0 < n < 2:
        return n
    for _ in range(n):
        if n in cache:
            return cache[n]
        cache[n] = fib_recursive(n - 1) + fib_recursive(n - 2)
    return cache[n]


def fib_non_recursive(n: int) -> int:
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def fib_tabulation(n: int) -> int:
    if n == 0:
        return 0
    if 0 < n < 2:
        return n
    table = [0] * (n + 1)
    table[1] = 1
    table[2] = 1
    for i in range(3, n + 1):
        table[i] = table[i - 1] + table[i - 2]
    return table[n]


if __name__ == "__main__":
    assert fib_recursive(7) == 13
    assert fib_recursive(0) == 0
    assert fib_recursive(1) == 1
    assert fib_recursive(2) == 1
    assert fib_recursive(17) == 1597
    assert fib_recursive(20) == 6765
    # assert fib_recursive(100) == 354224848179261915075
    assert fib_non_recursive(7) == 13
    assert fib_non_recursive(0) == 0
    assert fib_non_recursive(1) == 1
    assert fib_non_recursive(2) == 1
    assert fib_non_recursive(17) == 1597
    assert fib_non_recursive(20) == 6765
    assert fib_non_recursive(100) == 354224848179261915075
    assert fib_non_recursive(240) == 64202014863723094126901777428873111802307548623680
    assert fib_tabulation(7) == 13
    assert fib_tabulation(0) == 0
    assert fib_tabulation(1) == 1
    assert fib_tabulation(2) == 1
    assert fib_tabulation(3) == 2
    assert fib_tabulation(17) == 1597
    assert fib_tabulation(20) == 6765
    assert fib_tabulation(100) == 354224848179261915075
    assert fib_tabulation(240) == 64202014863723094126901777428873111802307548623680
