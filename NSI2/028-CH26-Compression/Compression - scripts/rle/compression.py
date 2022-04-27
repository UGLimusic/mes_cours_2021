__author__ = 'UGLi'

from image import *

def compresse(image):
    result = []
    temp = image.pixel[0][0]
    compteur = 0
    result.append(image.width)
    result.append(image.height)
    for i in range(0, image.width):
        for j in range(0, image.height):
            if image.pixel[i][j] == temp:
                compteur += 1
            else:
                result.append(temp)
                result.append(compteur)
                compteur = 1
                temp = image.pixel[i][j]
    return result


def decompresse(datas):
    result = Image()
    result.width = datas[0]
    result.height = datas[1]
    result.pixel = [[(0, 0, 0) for i in range(result.height)] for j in range(result.width)]
    k = 0
    l = 0
    i = 2
    while i < len(datas):
        for j in range(datas[i + 1]):
            result.pixel[k][l] = datas[i]
            l += 1
            if l == result.height:
                l = 0
                k += 1
        i += 2
    return result

# ###############
# MAIN   #
# ###############

image = Image()  # On crée une image vide
image.import_from("doudouchat.ppm")  # On la remplit avec un fichier ppm raw TrueColor
origSize = image.width * image.height * 3
res = compresse(image)
compSize = len(res) * 2-2

print(1-compSize/origSize)
image.display