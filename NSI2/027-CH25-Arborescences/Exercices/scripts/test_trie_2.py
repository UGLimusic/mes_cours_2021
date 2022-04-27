from trie import Trie


trie = Trie()
trie.ajoute_mot("SALUT")
trie.ajoute_mot("SALOPE")
print(trie.commence("SALU"))