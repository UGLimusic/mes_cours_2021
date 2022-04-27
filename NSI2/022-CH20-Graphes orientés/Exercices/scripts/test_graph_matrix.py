from graph_matrix import *


# On construit le graphe de l'exercice

try:
    G = GraphMatrix(4)
except:
    print("Erreur dans la méthode '__init__'.")

try:
    G.add_arrow(0, 1)
    G.add_arrow(0, 2)
    G.add_arrow(1, 2)
    G.add_arrow(1, 3)
    G.add_arrow(2, 0)
    G.add_arrow(2, 1)
    G.add_arrow(3, 0)
    G.add_arrow(3, 2)
except:
    print("Erreur dans la méthode 'add_arrow'.")

# On effectue des tests

if not G.is_predecessor(0,2):
    print("Erreur dans la méthode 'is_predecessor'.")
elif not G.is_successor(2,0):
    print("Erreur dans la méthode 'is_successor'.")
else:
    print(G.successors(0))
    print(G.predecessors(0))