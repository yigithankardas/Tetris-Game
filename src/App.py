from Window import Window
import pygame
from pygame.locals import *


class App:
    def __init__(self) -> "App":
        self.__running = True
        self.__window = None

    def __onInit(self) -> bool:
        pygame.init()
        self.__running = True
        self.__window = Window()

    def __onEvent(self, event):
        if event.type == pygame.QUIT:
            self.__running = False
            self.__window.close()

    def __onLoop(self):
        pass

    def __onRender(self):
        pass

    def __onCleanup(self):
        pass

    def __onExecute(self):
        if self.__onInit() == False:
            self.__running = False

        while (self.__running):
            for event in pygame.event.get():
                self.__onEvent(event)

            self.__onLoop()
            self.__onRender()

        self.__onCleanup()

    def execute(self) -> int:
        self.__onExecute()
