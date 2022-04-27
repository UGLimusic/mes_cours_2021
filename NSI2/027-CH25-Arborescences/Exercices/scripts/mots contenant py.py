
mots_py = []
with open('dico.txt', 'rt', encoding='utf8') as fichier:  # on ouvre le fichier
    ligne = fichier.readline()  # on lit une ligne
    while ligne:
        if 'PI' in ligne:
            mots_py.append(ligne[:-1])
        ligne = fichier.readline()

for mot in mots_py:
    print(mot)
