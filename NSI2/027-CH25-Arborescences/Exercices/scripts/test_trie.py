from trie import Trie


T = Trie()

T.ajoute_mot("salut")
T.ajoute_mot("sa")
T.ajoute_mot("sale")
print(T.nb_nodes)
