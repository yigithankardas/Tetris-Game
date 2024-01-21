import pygame
from pygame.locals import *


class Window:
    def __init__(self) -> "Window":
        self.__size = self.__weight, self.__height = 640, 400
        self.__window: pygame.Surface = pygame.display.set_mode(
            self.__size, pygame.HWSURFACE | pygame.DOUBLEBUF)

    def close(self) -> bool:
        return True
