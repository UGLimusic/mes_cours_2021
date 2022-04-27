from graph_dict import *

try:
    G = GraphDict(['A', 'B', 'C'])
except:
    print("Erreur dans la méthode '__init__'.")

try:
    G.add_arrow('A', 'B')
    G.add_arrow('A', 'C')
    G.add_arrow('B', 'C')
    G.add_arrow('C', 'A')
    G.add_arrow('C', 'B')
    G.add_vertex('D')
    G.add_arrow('D', 'A')
    G.add_arrow('D', 'C')
    G.add_arrow('B', 'D')
except:
    print("Erreur dans la méthode 'add_arrow'.")

# On effectue des tests

if not G.is_predecessor('A', 'C'):
    print("Erreur dans la méthode 'is_predecessor'.")
elif not G.is_successor('C', 'A'):
    print("Erreur dans la méthode 'is_successor'.")
else:
    print('Tout est OK.')

print(G.successors('A'))
print(G.predecessors('A'))
print(G.vertices())
