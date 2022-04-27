from PIL import Image
from random import randint


def scramble(img):
    """
    :param img: image
    :return: image
    """
    final_image = Image.new("RGB", img.size)
    final_pixels = final_image.load()
    pixels = img.load()
    for i in range(img.size[0]):
        k = (i // 2) * (i % 2 == 0) + (img.size[0] // 2 + (i - 1) // 2) * (i % 2 == 1)
        for j in range(img.size[1]):
            l = (j // 2) * (j % 2 == 0) + (img.size[1] // 2 + (j - 1) // 2) * (j % 2 == 1)
            final_pixels[k, l] = pixels[i, j]
    return final_image


img = Image.open("joconde_0.jpg")
pixels = img.load()

# for i in range(320):
#     for j in range(200):
#         pixels[i, j] = (randint(0, 255), randint(0, 255), randint(0, 255))

for i in range(9):
    img = scramble(img)
    img.show()
