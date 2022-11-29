#! /usr/bin/env python
import os, random, sys, math
import botonPalabra
import pygame
from pygame.locals import *
from configuracion import *
from extras import *
from funcionesVACIAS import *
import pygame
import pygame
from funcionesVACIAS import *
from pygame.locals import *
from configuracion import *
import funcionesVACIAS
import principal
import time

#Funcion principal
def main():
    #Centrar la ventana y despues inicializar pygame
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    pygame.mixer.init()

    #Preparar la ventana
    pygame.display.set_caption("La escondida...")
    screen = pygame.display.set_mode((ANCHO, ALTO))

    #tiempo total del juego
    gameClock = pygame.time.Clock()
    totaltime = 0
    segundos = TIEMPO_MAX
    fps = FPS_inicial

    usuarioModalidad = ""
    jugando = 0
    puntos = 0
    palabraUsuario = ""
    listaPalabrasDiccionario = []
    ListaDePalabrasUsuario = []
    correctas = []
    incorrectas = []
    casi = []
    gano = False
    archivo = open("lemario.txt","r")
    fail = pygame.mixer.Sound("fail.mp3")
    fail0 = pygame.mixer.Sound("incorrecta.mp3")
    victory = pygame.mixer.Sound("victory.mp3")
    victory0 = pygame.mixer.Sound("correcta.mp3")
    largoIncorrecto = pygame.mixer.Sound("largoIncorrecto.mp3")
    pygame.mixer.music.load('backgroundMusic.mp3')
    pygame.mixer.music.play(-1) 

    defaultFont = pygame.font.Font(pygame.font.get_default_font(), TAMANNO_LETRA)
    defaultFontGrande = pygame.font.Font(pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)
    defaultFontMediana = pygame.font.Font(pygame.font.get_default_font(), TAMANNO_LETRA_MEDIANA)
    
    pantallaInicial(screen)
    pygame.display.flip()

    while jugando == 0:
        for e in pygame.event.get():

            if e.type == pygame.KEYDOWN or e.type == KEYDOWN:
                print("Holiii")
                usuarioModalidad += dameLetraApretada(e.key)
                screen.blit(defaultFont.render(usuarioModalidad, 1, COLOR_TEXTO), (190, 570))
                print(usuarioModalidad)

                if usuarioModalidad != "a":
                    usuarioModalidad = ""

                if usuarioModalidad == "a":
                    pygame.mixer.music.stop()
                    usuarioModalidad = ""
                    print("Chau")
                    #lectura del diccionario
                    lectura(archivo, listaPalabrasDiccionario, LARGO)

                    #elige una al azar
                    palabraCorrecta = corregirPalabraCorrecta(nuevaPalabra(listaPalabrasDiccionario))

                    dibujar(screen, ListaDePalabrasUsuario, palabraUsuario, puntos, segundos, gano, correctas, incorrectas, casi, palabraCorrecta, 0)
                    print(palabraCorrecta)

                    while segundos > fps/1000 and not gano:

                    # 1 frame cada 1/fps segundos
                        gameClock.tick(fps)
                        totaltime += gameClock.get_time()

                        if True:
                            fps = 3

                        #Buscar la tecla apretada del modulo de eventos de pygame
                        for e in pygame.event.get():

                            #QUIT es apretar la X en la ventana
                            if e.type == QUIT:
                                pygame.quit()
                                return()

                            #Ver si fue apretada alguna tecla
                            if e.type == KEYDOWN:
                                letra = dameLetraApretada(e.key)
                                palabraUsuario += letra #es la palabra que escribe el usuario
                                if e.key == K_BACKSPACE:
                                    palabraUsuario = palabraUsuario[0:len(palabraUsuario)-1]
                                if e.key == K_RETURN:
                                    if len(palabraUsuario) != len(palabraCorrecta):
                                        pygame.mixer.Sound.play(fail)
                                        pygame.mixer.music.stop()
                                        pygame.mixer.Sound.play(largoIncorrecto)
                                        pygame.mixer.music.stop()
                                        palabraUsuario = ""
                                    else: 
                                        gano = revision(palabraCorrecta, palabraUsuario, correctas, incorrectas, casi)
                                        if gano:
                                            pygame.mixer.Sound.play(victory)
                                            pygame.mixer.music.stop()
                                            time.sleep(4)
                                            pygame.mixer.Sound.play(victory0)
                                            pygame.mixer.music.stop()
                                        else:
                                            if palabraUsuario not in ListaDePalabrasUsuario:
                                                ListaDePalabrasUsuario.append(palabraUsuario)
                                                pygame.mixer.Sound.play(fail)
                                                pygame.mixer.music.stop()
                                                pygame.mixer.Sound.play(fail0)
                                                pygame.mixer.music.stop()
                                            palabraUsuario = ""

                        segundos = TIEMPO_MAX - pygame.time.get_ticks()/1000

                        #Limpiar pantalla anterior
                        screen.fill(COLOR_FONDO)

                        #Dibujar de nuevo todo
                        dibujar(screen, ListaDePalabrasUsuario, palabraUsuario, puntos, segundos, gano, correctas, incorrectas, casi, palabraCorrecta, 1)

                        pygame.display.flip()

    while 1:
        #Esperar el QUIT del usuario
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                return

        archivo.close()
#Programa Principal ejecuta Main
if __name__ == "__main__":
    main()
