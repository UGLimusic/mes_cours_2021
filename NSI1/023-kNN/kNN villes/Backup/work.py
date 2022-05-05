import csv

# with open("departements_france.csv", encoding="utf8") as file:
#     csvreader = csv.reader(file)
#     content = []
#     next(csvreader)
#     for line in csvreader:
#         content.append(line[:2])
# print(content)
#
# with open("departements_francais.csv","wt",encoding="utf8",newline='') as write_file:
#     csvwriter = csv.writer(write_file)
#     csvwriter.writerows(content)
#
#
#
# with open("departements_francais.csv", encoding="utf8") as file:
#     csvreader = csv.reader(file)
#     content = []
#     for line in csvreader:
#         content.append(line)
#
# print(content)


with open("villes_france.csv", encoding="utf8") as file:
    line = [x.strip('"') for x in file.readline().split(',')]
    line = [x.strip('"') for x in file.readline().split(',')]

    content = []
    while len(line)>1:

        new_line = [line[1],line[3].capitalize(),float(line[19]),float(line[20])]
        if '0' not in new_line or line[1]==65:
            content.append(new_line)
        line = [x.strip('"') for x in file.readline().split(',')]
        if '0' in new_line :
            print(new_line)

with open("../villes_francaises.csv", "wt", encoding="utf8", newline='') as write_file:
    csvwriter = csv.writer(write_file)
    csvwriter.writerows(content)
