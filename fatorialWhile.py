def fatorial(n: int) -> int:
    i = 1
    fat = 1

    while i <= n:
        fat *= i
        i += 1

    return fat
