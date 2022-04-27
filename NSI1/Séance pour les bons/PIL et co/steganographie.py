from PIL import Image


def cache(image: Image, message: Image) -> Image:
    width, height = image.size
    im_pix = image.load()
    mess_pix = message.load()
    assert width, height == message.size("Les dimensions doivent être les mêmes.")
    result = Image.new("RGB", message.size)
    res_pix = result.load()
    for x in range(width):
        for y in range(height):
            r, g, b = im_pix[x, y]
            s = (r + g + b) % 2
            t = (mess_pix[x, y] == (0, 0, 0))
            if (t and s) or (not t and not s):
                b += 1
            res_pix[x, y] = (r, g, b)
    return result


def revele(image: Image) -> Image:
    width, height = image.size
    result = Image.new("RGB", image.size)
    res_pix = result.load()
    im_pix = image.load()
    for x in range(width):
        for y in range(height):
            cur_pix = im_pix[x, y]
            s = sum(cur_pix) % 2
            res_pix[x, y] = (255 * s, 255 * s, 255 * s)
    return result


img = Image.open("joconde_0.jpg")
mes = Image.open("message.png")
res = cache(img, mes)
res.show()
res2 = revele(res)
res2.show()
