#Jogo criado utilizando a Biblioteca Pygame
#A ideia do jogo é == ideia do jogo aqui ==

#Integrantes do grupo:
#Celina Melo e Lister Ogusuku

# Professor: Humberto Sandmann

#Link do vídeo: 

#Projeto Final | Design de Software | Insper 2021.1

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


#Importando as bibliotecas necessárias
import pygame
import os
import time
import random

pygame.font.init() #Inicializa as fontes do pygame para serem utilizadas no jogo

#Definindo altura e largura da janela do jogo
WIDTH, HEIGHT = 700, 700 #Dimensões do display
JANELA = pygame.display.set_mode((WIDTH, HEIGHT)) #Definição do display
pygame.display.set_caption("Projeto Final - DESIGN DE SOFTWARE") #Nome do jogo

