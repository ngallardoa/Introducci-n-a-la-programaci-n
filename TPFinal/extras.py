import pygame
from funcionesVACIAS import *
from pygame.locals import *
from configuracion import *

def dameLetraApretada(key):
    if key == K_a:
        return("a")
    elif key == K_b:
        return("b")
    elif key == K_c:
        return("c")
    elif key == K_d:
        return("d")
    elif key == K_e:
        return("e")
    elif key == K_f:
        return("f")
    elif key == K_g:
        return("g")
    elif key == K_h:
        return("h")
    elif key == K_i:
        return("i")
    elif key == K_j:
        return("j")
    elif key == K_k:
        return("k")
    elif key == K_l:
        return("l")
    elif key == K_m:
        return("m")
    elif key == K_n:
        return("n")
    elif key == K_o:
        return("o")
    elif key == K_p:
        return("p")
    elif key == K_q:
        return("q")
    elif key == K_r:
        return("r")
    elif key == K_s:
        return("s")
    elif key == K_t:
        return("t")
    elif key == K_u:
        return("u")
    elif key == K_v:
        return("v")
    elif key == K_w:
        return("w")
    elif key == K_x:
        return("x")
    elif key == K_y:
        return("y")
    elif key == K_z:
        return("z")
    elif key == K_SLASH:
        return("-")
    elif key == K_KP_MINUS:
        return("-")
    elif key == K_SPACE:
        return(" ")
    else:
        return("")


pygame.init()
defaultFont = pygame.font.Font(pygame.font.get_default_font(), TAMANNO_LETRA)
defaultFontGrande = pygame.font.Font(pygame.font.get_default_font(), TAMANNO_LETRA_GRANDE)
defaultFontCasiGrande = pygame.font.Font(pygame.font.get_default_font(), TAMANNO_LETRA_CASI_GRANDE)
defaultFontMediana = pygame.font.Font(pygame.font.get_default_font(), TAMANNO_LETRA_MEDIANA)

#muestra la pantalla con la que arranca el juego, para elegir las modalidades
def pantallaInicial(screen):
    pygame.draw.line(screen, (255,255,255), (0, ALTO-70) , (ANCHO, ALTO-70), 5)
    screen.blit(defaultFontMediana.render("Indique que modalidad quiere jugar", 1, COLOR_TEXTO), (20, 50))
    screen.blit(defaultFont.render("a - Por tiempo -> Tenés que adivinar la palabra lo antes posible", 1, COLOR_TEXTO), (40, 120))
    screen.blit(defaultFont.render("b - Por aciertos -> Tenés que adivinar la mayor cantidad de palabras", 1, COLOR_TEXTO), (40, 180))
    screen.blit(defaultFont.render("c - Por longitud -> La longitud de la palabra a adivinar es aleatoria", 1, COLOR_TEXTO), (40, 240))

def dibujar(screen, listaDePalabrasUsuario, palabraUsuario, puntos, segundos, gano, correctas, incorrectas, casi, palabraCorrecta):

    #Linea Horizontal
    pygame.draw.line(screen, (255,255,255), (0, ALTO-70) , (ANCHO, ALTO-70), 5)

    #muestra lo que escribe el jugador
    screen.blit(defaultFont.render(palabraUsuario, 1, COLOR_TEXTO), (190, 570))
    #muestra el puntaje
    screen.blit(defaultFont.render("Puntos: " + str(puntos), 1, COLOR_TEXTO), (680, 10))
    #muestra la longitud de la palabra
    screen.blit(defaultFont.render("La palabra tiene " + str(len(palabraCorrecta)) + " letras", 1, COLOR_TEXTO), (300, 10))
    #muestra los segundos y puede cambiar de color con el tiempo
    if (segundos < 15):
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TIEMPO_FINAL)
    else:
        ren = defaultFont.render("Tiempo: " + str(int(segundos)), 1, COLOR_TEXTO)
    screen.blit(ren, (10, 10))

    screen.blit(defaultFont.render("Correctas:", 1, COLOR_TEXTO), (60, 280))
    screen.blit(defaultFont.render("Casi correctas:", 1, COLOR_TEXTO), (60, 320))
    screen.blit(defaultFont.render("Incorrectas:", 1, COLOR_TEXTO), (60, 360))

    #muestra las palabras anteriores, las que se fueron arriesgando
    pos = 0
    for palabra in listaDePalabrasUsuario:
        screen.blit(defaultFontCasiGrande.render(palabra, 1, COLOR_LETRAS), (ANCHO//2-len(palabra)*TAMANNO_LETRA_CASI_GRANDE//4,20 + 80 * pos))
        pos += 1

    #muestra el abecedario, falta ponerle color a las letras
    abcdario = ["qwertyuiop", "asdfghjklm", "zxcvbnm"]
    y = 0
    for abc in abcdario:
        x = 0
        for letra in abc:
            color = COLOR_LETRAS
            screen.blit(defaultFont.render(letra, 1, color), (10 + x, ALTO/1.5 + y))
            x += TAMANNO_LETRA
        y += TAMANNO_LETRA
        
    #muestra las letras correctas, incorrectas y casi correctas
    a = 0
    b = 0
    c = 0
    if len(correctas) > 0 or len(casi) > 0 or len(incorrectas) > 0:
        for i in range(0, len(correctas)):
            screen.blit(defaultFont.render(correctas[i], 1, COLOR_CORRECTO), (240 + 10 * a, 280))
            a += 1
        for i in range(0, len(casi)):
            screen.blit(defaultFont.render(casi[i], 1, COLOR_CASI), (240 + 10 * b, 320))
            b += 1
        for i in range(0, len(incorrectas)):
            screen.blit(defaultFont.render(incorrectas[i], 1, COLOR_INCORRECTO), (240 + 10 * c, 360))
            c += 1







