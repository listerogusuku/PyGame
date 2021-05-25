#Jogo criado utilizando a Biblioteca Pygame
#A ideia do jogo é == ideia do jogo aqui ==

#Integrantes do grupo:
#Celina Melo e Lister Ogusuku

# Professor: Humberto Sandmann

#Link do vídeo: 

#Projeto Final | Design de Software | Insper 2021.1

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

#Assim como havíamos conversado, acho que nosso jogo pode atirar em zumbis ou criar
#tipo de uma competição entre brands, na qual uma destruiria a outra, entende?
#vamos conversar melhor sobre esses tópicos quando nos reunirmos, ok?
#Só estou escrevendo aqui para não nos esquecermos

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

def main(): #Função principal
    anda = True
    FPS = 60
    fase = 0
    vidas = 5
    texto_inicio = pygame.font.SysFont("Arial", 50) #Escolhemos a fonte Arial por ser uma fonte padrão
    texto_quando_perde = pygame.font.SysFont("Arial", 60) #não achei a fonte tão legal, vc não acha que seria melhor uma mais estilo game?

    inimigos = [] #precisamos definir os inimigos!!!
    alcance_do_inimigo = 5
    velocidade_do_inimigo = 1

    velocidade_do_jogador = 5
    velocidade_da_bala = 5

    jogador = Jogador(300, 630) #criar classe do jogador

    temporizador = pygame.time.Clock()

    perdeu = False
    contada_perdas = 0 #não entendi o que vc quis dizer aqui

