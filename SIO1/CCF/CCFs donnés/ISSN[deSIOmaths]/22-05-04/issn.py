def calcN(code7: str) -> int:
    m = 8
    N = 0
    for i in range(7):
        N += m * int(code7[i])
        m -=1
    return N


def calcCle(N: int) -> str:
    r = N % 11
    if not r:
        return '0'
    elif r == 1:
        return 'X'
    else:
        return str(11 - r)


def ISSNok(code8: str) -> bool:
    code7 = code8[:7]
    cle = code8[7]
    N = calcN(code7)
    if cle == calcCle(N):
        return True
    else:
        return False

def bonus(code8:str) -> None:
    code6= code8[1:7]
    for i in range(10):
        code_variant = str(i)+code6
        print(f"Pour {code_variant} on trouve une clé de {calcCle(calcN(code_variant))}.")


mon_code = "03952037"
bonus(mon_code)
