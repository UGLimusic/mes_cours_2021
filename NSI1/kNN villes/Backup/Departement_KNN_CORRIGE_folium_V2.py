"""
Objectif : Déterminer dans quel département se situe une position GPS
avec une indication sur le pourcentage de fiabilité.

Principe : Utilisation de l'algorithme des K plus proches voisins

Etapes :
1 - Demander les coordonnées GPS de la localisation
2 - Lecture du fichier CSV pour extraire "Nom", "GPS", "Code_postal"
3 - Calculer les distances
4 - Ne retenir QUE les k plus proches villes
5 - Déterminer les départements des k plus proches villes
6 - Déterminer une probabilité de localisation


A creuser (source : https://www.pythonpool.com/python-csv-dictreader/ ):
def UnicodeDictReader(utf8_data, **kwargs):
    csv_reader = csv.DictReader(utf8_data, **kwargs)
    for row in csv_reader:
        yield {unicode(key, 'utf-8'):unicode(value, 'utf-8') for key, value in row.iteritems()}
"""
from math import sqrt, sin, cos, acos, pi
from csv import DictReader
import folium  # Bibliothèque pour créer un fond de carte

KNN = 9  # Algorithme des 5 plus proches villes


# ======================================================== positions
def positions(fichier_villes: str) -> dict:
    """ Retourne un dictionnaire { Numéro:[ville, codePost, (coordonnées GPS)] } """
    """ num, Slug, Nom, NomSimple,NomReel,NomSound,NomMeta,CodePostal,
    NumCommune,CodeCommune,INSEE,Arrond, Canton,Pop2010,Pop1999,Pop2012,
    Dens2010,Superf,GPS_Long,GPS_Lat,LongGRD,LatGRD,LongDMS,LatDMS,AltMin,AltMax"""
    with open(fichier_villes, "r") as fichier:
        data = DictReader(fichier, delimiter=',')
        villes = {}
        num = 0
        for one in data:
            position = one["GPS_Lat"] + "," + one["GPS_Long"]
            villes.update({num: {"Nom": one["NomReel"],
                                 "CP": one["CodePostal"],
                                 "GPS": position}})
            num += 1
    return villes


# ======================================================== distance
def distance(coord1: tuple, coord2: tuple) -> float:
    """ Correction orthodromique de la distance entre deux points à la surface de la Terre
    Entrée : coord1, coord2 -> coordonnées GPS
    Sortie : distance parcourue en km entre coord1 et coord2
    """
    lat1, long1 = coord1
    lat2, long2 = coord2
    rlat1 = pi * lat1 / 180  # conversion des angles degré -> radian
    rlat2 = pi * lat2 / 180
    rlon1 = pi * long1 / 180
    rlon2 = pi * long2 / 180

    theta = long1 - long2;
    rtheta = pi * theta / 180

    dist = sin(rlat1) * sin(rlat2) + cos(rlat1) * cos(rlat2) * cos(rtheta);
    dist = acos(dist);
    dist = dist * 180 / pi;
    dist = dist * 60 * 1.1515;
    dist = dist * 1.609344
    return dist


# ======================================================== ajouter_ville
def ajouter_ville(knn_villes: list, ville: dict, d: float, knn: int) -> None:
    """ knn_ville -> [ { "d", "Nom", "CP", "GPS" } ]
    Modification en place de la liste 'knn_ville' pour insérer
    la 'ville' si la distance 'd' est inférieure à une distance déjà
    présente dans la liste.
    La longueur de la liste est limitée à knn villes.
    La liste est maintenue par ordre croissant d'éloignement. """
    if len(knn_villes) < 2:  # Ajouter les deux première villes
        knn_villes.append({"d": d,
                           "Nom": ville["Nom"],
                           "CP": ville["CP"],
                           "GPS": ville["GPS"]})
    else:
        d_max = knn_villes[-1]["d"]  # Comparer avec la ville la plus éloignée
        if d < d_max:
            for i in range(len(knn_villes)):
                if d < knn_villes[i]["d"]:  # Insérer une ville plus proche
                    if ville["Nom"] != knn_villes[i - 1]["Nom"]:
                        knn_villes.insert(i, {"d": d,
                                              "Nom": ville["Nom"],
                                              "CP": ville["CP"],
                                              "GPS": ville["GPS"]})
                    break
        if len(knn_villes) > knn:  # Limiter le nombre de villes à knn
            knn_villes.pop(-1)


# ======================================================== ajouter_departement
def ajouter_departement(knn_villes: list, departements: str) -> None:
    """ Modification en place de la liste knn_villes pour ajouter le département
    à chacune des villes les plus proches """
    with open(departements, "r") as dep_file:
        for i in range(len(knn_villes)):  # Pour chaque ville
            code_dep = knn_villes[i]["CP"][:2]
            dep_dict = DictReader(dep_file, delimiter=',')
            # {code_departement,nom_departement,code_region,nom_region}
            for one_dep in dep_dict:
                # Ajouter le département au nom de la ville
                if one_dep["code_departement"] == code_dep:
                    knn_villes[i].update({"Dep": one_dep["nom_departement"]})
                    break
            dep_file.seek(0)  # Retour au début du fichier


# ======================================================== ajouter_departement
def proba_departements(knn_villes: list) -> dict:
    """ Reçoit la liste des KNN villes les plus proches :
    { 'd', 'Nom', 'CP', GPS', 'Dep' }
    Renvoie les différents départements avec % de confiance.
    Le % de confiance est calculé en fonction de l'inverse des distances.
    Plus une ville est proche plus le % de confiance sera élevé.
    La plus proche -> KNN points, ensuite KNN-1, ... ,puis 1 """
    n = len(knn_villes)
    nb_pts = n
    list_dep = {}
    for ville in knn_villes:  # Pour chaque ville
        # Si une des distances est < 1km, on est sûr à 100% d'être dans son département
        if ville['d'] < 1:
            return {ville['Dep']: 100}

        if ville['Dep'] not in list_dep.keys():  # Regrouper par département
            list_dep[ville['Dep']] = nb_pts
        else:
            list_dep[ville['Dep']] += nb_pts
        nb_pts -= 1

    for ville in list_dep.items():
        print(ville)

    tot_pts = (1 + n) * n / 2

    for dep in list_dep.keys():  # Pour chaque département
        list_dep[dep] = round((list_dep[dep] / tot_pts) * 100)  # calculer la probabilité

    return list_dep


# ====================================================================
# =============================================================== Main

# 1 - Demander les coordonnées GSP de la localisation
# Angers :
# position =  47.476657084, -0.556221025
# La Basse Ambaudière (Maine-et-Loire)
position =  47.786067, -1.232753
#position =48.52081791334807, -2.8153650094762797
# 2 - Lecture du fichier CSV pour extraire "Nom", "Code_postal", "GPS"
# villes = positions ("laposte.csv")
villes = positions("villes_france.csv")

# 3 - Calculer les distances
# 4 - Ne retenir QUE les k plus proches villes
knn_villes = []
for ville in villes.values():
    GPS_str = ville["GPS"].split(",")
    if "." in GPS_str[0] and "." in GPS_str[1]:
        # Ne pas prendre en compte les DOMTOM pcq pas de localisation GPS :-(
        GPS = float(GPS_str[0]), float(GPS_str[1])
        d = distance(position, GPS)
        ajouter_ville(knn_villes, ville, d, KNN)
        # Si une des distances est < 1km, on est sûr à 100% d'être dans son département
        if d < 1:
            break

# 5 - Déterminer les départements des k plus proches villes
ajouter_departement(knn_villes, "departements_france.csv")

# 6 - Déterminer une probabilité de localisation
result = proba_departements(knn_villes)

# Créer la carte intitulée MonParcours
carte = folium.Map(position, zoom_start=13, tiles='OpenStreetMap')

print("Position entrée :", position)
for dep in result.items():
    print(dep[0], " -> ", dep[1], "%")

location = position[0], position[1]
folium.Marker(location, icon=folium.Icon(color="green", icon="flag"), popup='Vous êtes ici !').add_to(carte)

for ville in knn_villes:
    # Pour chaque enregistrement GPS, placer un marqueur
    gps = ville["GPS"].split(',')
    location = (float(gps[0]), float(gps[1]))
    folium.Marker(location, icon=folium.Icon(color="red"), popup=ville['Nom']).add_to(carte)
# Enregistrer la carte au format html pour l'ouvrir avec FireFox par exemple
carte.save(outfile='carte.html')
