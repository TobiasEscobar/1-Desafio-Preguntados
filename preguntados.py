import pygame
from constantes import *
from funciones import * 
from os import system
system("cls")

pygame.init()
#Pantalla
pantalla = pygame.display.set_mode((ANCHO_VENTANA, ALTO_VENTANA))
pygame.display.set_caption("Desafio Preguntados")

icono = pygame.image.load("Primer_Parcial/imagenes_parcial/icono.png")
pygame.display.set_icon(icono)

fondo = pygame.image.load("Primer_Parcial/imagenes_parcial/preguntados_fondo.jpg")
fondo_final = pygame.transform.scale(fondo, (ANCHO_VENTANA, ALTO_VENTANA))

imagen = pygame.image.load("Primer_Parcial/imagenes_parcial/icono.png")
imagen_final = pygame.transform.scale(imagen, (200, 200))

#Texto
fuente_1 = pygame.font.SysFont("Arial", 20)
fuente_2 = pygame.font.SysFont("Arial", 40)

posicion = 0
preguntas = guardar_en_sub_listas(lista)

flag_borra_opcion = True
vacio = ""

flag_siguiente_pregunta = False

#Sumar puntos y errores
score_puntos = 0
flag_punto_sumado = True
contar_errores = 0

pregunta_actual = preguntas[posicion]
texto_pregunta = fuente_1.render(pregunta_actual[0], True, COLOR_NEGRO)
texto_opciones_a = fuente_1.render("a: " + pregunta_actual[1], True, COLOR_NEGRO)
texto_opciones_b = fuente_1.render("b: " + pregunta_actual[2], True, COLOR_NEGRO)
texto_opciones_c = fuente_1.render("c: " + pregunta_actual[3], True, COLOR_NEGRO)

flag_seguir = True
while flag_seguir:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            flag_seguir = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            posicion_click = list(evento.pos)
            if 50 <= posicion_click[0] <= 250 and 500 <= posicion_click[1] <= 560:
                if flag_siguiente_pregunta == True:
                    posicion += 1
                    flag_siguiente_pregunta = False
                    contar_errores = 0
                    if posicion >= len(preguntas):
                        posicion = 0
                
                pregunta_actual = preguntas[posicion]
                texto_pregunta = fuente_1.render(pregunta_actual[0], True, COLOR_NEGRO)
                texto_opciones_a = fuente_1.render("a: " + pregunta_actual[1], True, COLOR_NEGRO)
                texto_opciones_b = fuente_1.render("b: " + pregunta_actual[2], True, COLOR_NEGRO)
                texto_opciones_c = fuente_1.render("c: " + pregunta_actual[3], True, COLOR_NEGRO)

                flag_borra_opcion = True
                flag_punto_sumado = True
            
            elif 550 <= posicion_click[0] <= 750 and 500 <= posicion_click[1] <= 560:
                score_puntos = 0
                posicion = 0
                pregunta_actual = preguntas[posicion]
                texto_pregunta = fuente_1.render(pregunta_actual[0], True, COLOR_NEGRO)
                texto_opciones_a = fuente_1.render("a: " + pregunta_actual[1], True, COLOR_NEGRO)
                texto_opciones_b = fuente_1.render("b: " + pregunta_actual[2], True, COLOR_NEGRO)
                texto_opciones_c = fuente_1.render("c: " + pregunta_actual[3], True, COLOR_NEGRO)

            #Opcion A
            elif 50 <= posicion_click[0] <= 200 and 391 <= posicion_click[1] <= 437:
                if pregunta_actual[4] == "a" and flag_borra_opcion == True and flag_punto_sumado == True:
                    score_puntos += 10
                    contar_errores = 2
                    #Flags
                    flag_siguiente_pregunta = True
                    flag_punto_sumado = False
                    flag_borra_opcion = False
                    #Texto
                    texto_opciones_a = fuente_1.render(vacio, True, COLOR_NEGRO)
                    texto_opciones_b = fuente_1.render(vacio, True, COLOR_NEGRO)
                    texto_opciones_c = fuente_1.render(vacio, True, COLOR_NEGRO)
                else:
                    texto_opciones_a = fuente_1.render(vacio, True, COLOR_NEGRO)
                    contar_errores += 1
                    flag_siguiente_pregunta = False
                    if contar_errores >= 2:
                        #Flags
                        flag_punto_sumado = False
                        flag_borra_opcion = False
                        flag_siguiente_pregunta = True
                        #Texto
                        texto_opciones_b = fuente_1.render(vacio, True, COLOR_NEGRO)
                        texto_opciones_c = fuente_1.render(vacio, True, COLOR_NEGRO)

            #Opcion B
            elif 326 <= posicion_click[0] <= 476 and 391 <= posicion_click[1] <= 437:
                if pregunta_actual[4] == "b" and flag_borra_opcion == True and flag_punto_sumado == True:
                    score_puntos += 10
                    contar_errores = 2
                    #Flags
                    flag_siguiente_pregunta = True
                    flag_punto_sumado = False
                    flag_borra_opcion = False
                    #Texto
                    texto_opciones_a = fuente_1.render(vacio, True, COLOR_NEGRO)
                    texto_opciones_b = fuente_1.render(vacio, True, COLOR_NEGRO)
                    texto_opciones_c = fuente_1.render(vacio, True, COLOR_NEGRO)
                else:
                    texto_opciones_b = fuente_1.render(vacio, True, COLOR_NEGRO)
                    contar_errores += 1
                    flag_siguiente_pregunta = False
                    if contar_errores >= 2:
                        #Flags
                        flag_punto_sumado = False
                        flag_borra_opcion = False
                        flag_siguiente_pregunta = True
                        #Texto
                        texto_opciones_a = fuente_1.render(vacio, True, COLOR_NEGRO)
                        texto_opciones_c = fuente_1.render(vacio, True, COLOR_NEGRO)
            
            #Opcion C
            elif 611 <= posicion_click[0] <= 762 and 391 <= posicion_click[1] <= 437:
                if pregunta_actual[4] == "c" and flag_borra_opcion == True and flag_punto_sumado == True:
                    score_puntos += 10
                    contar_errores = 2
                    #Flags
                    flag_siguiente_pregunta = True
                    flag_punto_sumado = False
                    flag_borra_opcion = False
                    #Texto
                    texto_opciones_a = fuente_1.render(vacio, True, COLOR_NEGRO)
                    texto_opciones_b = fuente_1.render(vacio, True, COLOR_NEGRO)
                    texto_opciones_c = fuente_1.render(vacio, True, COLOR_NEGRO)
                else:
                    texto_opciones_c = fuente_1.render(vacio, True, COLOR_NEGRO)
                    contar_errores += 1
                    flag_siguiente_pregunta = False
                    if contar_errores >= 2:
                        #Flags
                        flag_punto_sumado = False
                        flag_borra_opcion = False
                        flag_siguiente_pregunta = True
                        #Texto
                        texto_opciones_a = fuente_1.render(vacio, True, COLOR_NEGRO)
                        texto_opciones_b = fuente_1.render(vacio, True, COLOR_NEGRO)
    # Imágenes
    pantalla.blit(fondo_final, (0, 0))
    pantalla.blit(imagen_final, (10, 10))

    # Pregunta y opciones
    pygame.draw.rect(pantalla, COLOR_VERDE_AGUA, (180, 270, 480, 50))
    pygame.draw.rect(pantalla, COLOR_VERDE_AGUA, (50, 390, 153, 50))
    pygame.draw.rect(pantalla, COLOR_VERDE_AGUA, (325, 390, 153, 50))
    pygame.draw.rect(pantalla, COLOR_VERDE_AGUA, (610, 390, 153, 50))
    pantalla.blit(texto_pregunta, (200, 280))
    pantalla.blit(texto_opciones_a, (60, 400))
    pantalla.blit(texto_opciones_b, (335, 400))
    pantalla.blit(texto_opciones_c, (620, 400))

    # Botones Pregunta y reiniciar
    boton_pregunta = fuente_2.render("Pregunta", True, COLOR_NEGRO)
    boton_reiniciar = fuente_2.render("Reiniciar", True, COLOR_NEGRO)
    pygame.draw.rect(pantalla, COLOR_VERDE_AGUA, (50, 500, 200, 60))
    pygame.draw.rect(pantalla, COLOR_VERDE_AGUA, (550, 500, 200, 60))
    pantalla.blit(boton_pregunta, (80, 505))
    pantalla.blit(boton_reiniciar, (588, 505))

    # Score
    vista_score = fuente_2.render("Score: " + str(score_puntos), True, COLOR_NEGRO)
    pygame.draw.rect(pantalla, COLOR_VERDE_AGUA, (600, 20, 170, 50))
    pantalla.blit(vista_score, (600, 20))

    pygame.display.flip()

pygame.quit()