from time import perf_counter
from random import randint


def get_execution_time(f):
    def wrapper(x):
        print("start")
        start = perf_counter()
        result = f(x)
        input(f"Execution time : {perf_counter() - start}s.")
        return result
    return wrapper


@get_execution_time
def tous_pairs1(lst: list) -> bool:
    resultat = True
    for x in lst:
        if x % 2 == 1:
            resultat = False
    return resultat


@get_execution_time
def tous_pairs2(lst: list) -> bool:
    for x in lst:
        if x % 2 == 1:
            return False
    return True


@get_execution_time
def tous_pairs3(lst: list) -> bool:
    produit = 1
    for x in lst:
        produit *= x
    if produit % 2 == 1:
        return False
    else:
        return True


n = int(10e7
        )

test_lst = [randint(0, 1) for i in range(n)]
print("GO")
tous_pairs1(test_lst)
tous_pairs2(test_lst)
tous_pairs3(test_lst)
