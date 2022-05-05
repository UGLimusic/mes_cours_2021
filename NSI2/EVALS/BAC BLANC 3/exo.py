



def construireDict(listeLiaisons):
    Dict = {}
    for liaison in listeLiaisons: # + [[y, x] for [x, y] in listeLiaisons]:
        villeA = liaison[0]
        villeB = liaison[1]
        if not villeA in Dict.keys():
            Dict[villeA] = [villeB]
        else:
            destinationsA = Dict[villeA]
            if not villeB in destinationsA:
                destinationsA.append(villeB)
        if not villeB in Dict.keys():
            Dict[villeB] = [villeA]
        else:
            destinationsB = Dict[villeB]
            if not villeA in destinationsB:
                destinationsB.append(villeA)
    return Dict


liaisonsJoueur1 = [
    ["Toulouse", "Muret"],
    ["Toulouse", "Montauban"],
    ["Gaillac", "St Sulpice"],
    ["Muret", "Pamiers"]
]

print(construireDict(liaisonsJoueur1))
