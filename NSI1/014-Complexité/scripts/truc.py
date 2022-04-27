print('salut')
n = int(10e6)

test_lst = [(i ** 2 + 2 * i + 1) % 2 for i in range(n)]

print('salut')
resultat = True
for x in test_lst:
    if x % 2 == 1:
        resultat = False


print(resultat)
