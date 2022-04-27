def f(L: list) -> int:
    mini = L[0]
    n = len(L)
    for i in range(n):
        if L[i] < mini:
            mini = L[i]
    return mini
