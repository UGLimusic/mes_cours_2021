from construit_liste import liste_mots
from anagrammes import scrabble
from time import process_time

ana = scrabble('VERSEAU')
print(ana)
print("Début du programme.")
start = process_time()
for mot in ana:
    if mot in liste_mots:
        print(mot)
print(f"temps d'execution en millisecondes : {(process_time()-start)*1000}")