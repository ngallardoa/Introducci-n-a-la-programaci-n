import pygame
from configuracion import *

screen = pygame.display.set_mode((ANCHO, ALTO))

class Boton():
    def __init__(self, x, y, imagen, escala):
        ancho = imagen.get_width()
        alto = imagen.get_height()
        self.imagen = pygame.transform.scale(imagen, (int(ancho * escala), int(alto * escala)))
        self.rect = self.imagen.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        acción = False
        posición = pygame.mouse.get_pos()

        if self.rect.collidepoint(posición):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                acción = True

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        screen.blit(self.imagen,(self.rect.x, self.rect.y))

        return acción