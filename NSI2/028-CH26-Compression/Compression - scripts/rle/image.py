__author__ = 'UGLi'
import pygame
from pygame.locals import *
from copy import *

class Image:
    """

    """

    def __init__(self):

        self._width = self._height = 0
        self.pixel = []

    def create(self):
        self.pixel = [[(0, 0, 0) for i in range(self._height)] for j in range(self._width)]

    def import_from(self, filename):
        """
        :param filename: a RAW PPM file
        :width: int
        :height: int
        :pixel: a width x height list of 3uples
        """
        file = open(filename, 'rb')
        rawcontent = file.read()
        i = 0
        content = []
        for j in range(4):
            content.append('')
            while rawcontent[i] != 10:
                content[j] += chr(rawcontent[i])
                i += 1
            i += 1
        self._width = int(content[2].split(' ')[0])
        self._height = int(content[2].split(' ')[1])
        content = rawcontent[i:]
        self.pixel = [[(0, 0, 0) for i in range(self._height)] for j in range(self._width)]
        for j in range(self._height):
            for i in range(self._width):
                pixcol = [
                    content[3 * i + self._width * 3 * j], content[3 * i + 1 + self._width * 3 * j],
                    content[3 * i + 2 + self._width * 3 * j]]
                self.pixel[i][j] = pixcol

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    def _display(self):
        pygame.init()

        # set up the window
        displaysurf = pygame.display.set_mode((self._width, self._height), 0, 24)
        pygame.display.set_caption('Drawing')
        pixobj = pygame.PixelArray(displaysurf)
        for j in range(self._height):
            for i in range(self._width):
                pixobj[i][j] = tuple(self.pixel[i][j])
        del pixobj
        pygame.display.update()
        # run the game loop
        loop = True
        while loop:
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    loop = False

    @property
    def display(self):
        return self._display()

copie = deepcopy