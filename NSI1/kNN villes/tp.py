import csv

nb_voisins = 5


def distance_carre(t: tuple, v: list) -> tuple:
    xa, ya = t
    xb, yb = float(v[2]), float(v[3])
    return v[0], v[1], (xb - xa) ** 2 + (yb - ya) ** 2


def kNN(t: tuple) -> dict:
    distances = [distance_carre(t, v) for v in villes]
    distances.sort(key=lambda x: x[2])
    temp_result = dict()
    for i in range(nb_voisins):
        if distances[i][0] not in temp_result:
            temp_result[distances[i][0]] = 0
        temp_result[distances[i][0]] += 1

    return {departements[i]: round((temp_result[i] / nb_voisins * 100), 2) for i in temp_result}


with open("departements_francais.csv", "rt", encoding="utf8") as read_file:
    reader = csv.reader(read_file)
    departements = dict()
    for line in reader:
        departements[line[0]] = line[1]

with open("villes_francaises.csv", "rt", encoding="utf8") as read_file:
    reader = csv.reader(read_file)
    villes = []
    for line in reader:
        villes.append(line)
print(kNN((-1.232753,47.786067)))

