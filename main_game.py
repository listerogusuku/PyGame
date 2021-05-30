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
WIDTH, HEIGHT = 700, 700 #Dimensões da tela
JANELA = pygame.display.set_mode((WIDTH, HEIGHT)) #Definição do display
pygame.display.set_caption("Kill Covid Game") #Nome do jogo

#Imagens que vão ser utilizadas
VIRUS_VERMELHO = pygame.image.load(os.path.join("caveira_virus.png")) #Vírus Caveira Vermelha
VIRUS_ERRO = pygame.image.load(os.path.join("erro_404_2.png")) #Erro 404
VIRUS_TROJAN = pygame.image.load(os.path.join("trojan.png")) #Trojan / Cavalo de Tróia

#Defesa do Jogador
mcafee = pygame.image.load(os.path.join("mcafee.png")) #Defesa do jogador ==> Logotipo do antivírus McAfee

#Contaminação/Problemas:
CONTAMINACAO_CAVEIRA = pygame.image.load(os.path.join("laser_virus_vermelho_robozinho.png")) #caveira da morte vírus
CONTAMINACAO_ERRO = pygame.image.load(os.path.join("laser_virus_preto_robozinho.png")) #Erro lançado
CONTAMINACAO_AMARELA = pygame.image.load(os.path.join("laser_virus_amarelo_trojan.png")) #trojan contaminando
ANTIVIRUS = pygame.image.load(os.path.join("remedio_antivirus.png")) #remédio do antivírus

#Fundo do jogo
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("background_tech.png")), (WIDTH, HEIGHT)) #fundo do jogo (POR ENQUANTO TEMPORÁRIO, PODEREMOS ALTERAR EM BREVE PARA UM MELHOR!!!)
#Eu também coloquei algumas imagens que, se você quiser, podemos alterar, mas achei bonitinho para o início
#Se for necessário, eu consigo fazer outras imagens também


#Orientação dos vírus
class Virus:
    def __init__(self, x, y, img):
        self.x = x
        self.y = y
        self.img = img
        self.mask = pygame.mask.from_surface(self.img)
#Desenhando a janela do jogo
    def desenhar(self, janela_game):
        janela_game.blit(self.img, (self.x, self.y))
#Definindo os movimentos
    def movimentacao(self, vel):
        self.y += vel

    def fora_da_tela(self, height):
        return not(self.y <= height and self.y >= 0)

    def impacto(self, obj):
        return colisao(self, obj)


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

