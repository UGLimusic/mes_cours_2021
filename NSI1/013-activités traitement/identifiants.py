import csv

from random import choice, randint

villes = ['Paris', 'Marseille', 'Toulouse', 'Bordeaux', 'Lyon']

sexe = ['femme', 'homme']

annee = list(range(1963, 2000))

syla = ["B", "BR", "BL", "C", "CH", "CL", "CR", "D", "DR", "H", "HER", "HEB", "HEC", "HEF", "J", "K", "L", "M", "N",
        "P", "PL", "PR", "R", "S", "SC", "ST", "SL", "T", "TR", "V", "VR"]
sylb = ["A", "E", "I", "O", "U", "Y", "IO", "OUI", "IN", "ION", "IAN", "IUN", "UN", "OU", "IO", "EUI"]
sylc = ["LE", "CE", "CHE", "NT", "RE", "X", "TEL", "NIEUX", "S", "SSE", "SC", "CO","THIAUX","NARD","TEC"]


def nom():
    a = choice(syla) + choice(sylb)

    return a + choice(sylc)


listing = []
for i in range(530):
    listing.append([nom(), choice(sexe), choice(annee), choice(villes)])

import csv

with open('personnel.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=',',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for line in listing:
        spamwriter.writerow(line)
print(listing)
