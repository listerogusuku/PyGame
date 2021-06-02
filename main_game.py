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

#Definindo os movimentos e velocidades para não sair da tela
    def movimentacao(self, vel):
        self.y += vel

    def fora_da_tela(self, height):
        return not(self.y <= height and self.y >= 0)

    def impacto(self, obj):
        return colisao(self, obj)


#Criação de uma orientação a objetos da Nave (Anti-vírus) com várias funções definidas
#para desenhar, mover, atirar e outras funcionalidades do jogo

class MCAFEE: #Classe do antivírus
    espera = 30 #coloquei 30 de espera, mas se você quiser, pode mudar
    def __init__(self, x, y, health=100): #Health é a "saúde" ou "quantidade de vida"
        self.x = x
        self.y = y
        self.health = health
        self.nave_img = None
        self.laser_img = None
        self.lasers = []
        self.contador_tempo_espera = 0

    def desenhar(self, janela_game):
        janela_game.blit(self.nave_img, (self.x, self.y))
        for laser in self.lasers:
            laser.desenhar(janela_game)

    def move_lasers(self, vel, obj):
        self.tempo_espera()
        for laser in self.lasers:
            laser.movimentacao(vel)
            if laser.fora_da_tela(HEIGHT):
                self.lasers.remove(laser)
            elif laser.impacto(obj):
                obj.health -= 10 #perde 10
                self.lasers.remove(laser)
    
    def tempo_espera(self): #Define tempo de espera
        if self.contador_tempo_espera >= self.espera:
            self.contador_tempo_espera = 0
        elif self.contador_tempo_espera > 0:
            self.contador_tempo_espera += 1

    def atirar(self): #Função designada para atirar
        if self.contador_tempo_espera == 0:
            laser = Virus(self.x, self.y, self.laser_img)
            self.lasers.append(laser)
            self.contador_tempo_espera = 1

    def get_width(self):
        return self.nave_img.get_width()

    def get_height(self):
        return self.nave_img.get_height()

#Class que orienta as ações tomadas pelo nosso jogador principal, representado pelo antivírus McAfee
class Jogador(MCAFEE):
    def __init__(self, x, y, health=500):
        super().__init__(x, y, health)
        self.nave_img = mcafee
        self.laser_img = ANTIVIRUS
        self.mask = pygame.mask.from_surface(self.nave_img)
        self.max_health = health

    def move_lasers(self, vel, objs):
        self.tempo_espera()
        for laser in self.lasers:
            laser.movimentacao(vel)
            if laser.fora_da_tela(HEIGHT):
                self.lasers.remove(laser)
            else:
                for obj in objs:
                    if laser.impacto(obj): #criação do if para o momento do impacto
                        objs.remove(obj) #remoção do obj em caso de impacto
                        if laser in self.lasers:
                            self.lasers.remove(laser)

    def desenhar(self, janela_game):  #Essa é a janelinha de vidas que a gente conversou no atendimento?
        super().desenhar(janela_game)
        self.barra_de_vidas(janela_game) #Janelinha da barra de vidas

#Criação da barrinha de vidas que ainda há disponível
    def barra_de_vidas(self, janela_game): #Vida disponível
        pygame.draw.rect(janela_game, (255, 0, 0), (self.x, self.y + self.nave_img.get_height() + 12, self.nave_img.get_width(), 12))
        pygame.draw.rect(janela_game, (0, 0, 255), (self.x, self.y + self.nave_img.get_height() + 12, self.nave_img.get_width() * (self.health/self.max_health), 12))

#Class dos vírus contaminantes com variação na cor deles, pra deixar mais atraente e bonitinho para o jogo
class Inimigo(MCAFEE):
    COR_MAP = {
                "caveira": (VIRUS_VERMELHO, CONTAMINACAO_CAVEIRA),
                "erro": (VIRUS_ERRO, CONTAMINACAO_ERRO),
                "trojan": (VIRUS_TROJAN, CONTAMINACAO_AMARELA)
                }

    def __init__(self, x, y, cor, health=100):
        super().__init__(x, y, health)
        self.nave_img, self.laser_img = self.COR_MAP[cor]
        self.mask = pygame.mask.from_surface(self.nave_img)

    def movimentacao(self, vel):
        self.y += vel

    def atirar(self):
        if self.contador_tempo_espera == 0:
            laser = Virus(self.x-20, self.y, self.laser_img)
            self.lasers.append(laser)
            self.contador_tempo_espera = 1

def colisao(obj1, obj2): #Define a colisão dos objetos
    desloc_x = obj2.x - obj1.x #Deslocamento em x
    desloc_y = obj2.y - obj1.y #Deslocamento em y
    return obj1.mask.overlap(obj2.mask, (desloc_x, desloc_y)) != None  #retorna objetos

def main(): #Função principal do nosso jogo
    anda = True
    FPS = 100
    fase = 0
    vidas = 10
    texto_inicio = pygame.font.SysFont("Cooper Black", 30) #Achei essa fonte mais legal que as outras para o estilo do jogo. Se
                                                           #você não gostar mutio ou encontrar outra melhor, me fala
    texto_quando_perde = pygame.font.SysFont("Cooper Black", 40)

    inimigos = []
    alcance_do_inimigo = 3
    velocidade_do_inimigo = 2

    velocidade_do_jogador = 5
    velocidade_do_laser = 5

    jogador = Jogador(300, 630)

    temporizador = pygame.time.Clock()

    perdeu = False
    contador_perdeu = 0


#TODO ESSE TRECHO ABAIXO É BASEADO NO HANDOUT DO PYGAME, ENTÃO PRECISAMOS ADAPTAR PARA NOSSO JOGO:

# ===== Loop principal =====
pygame.mixer.music.play(loops=-1)
while game:
    clock.tick(FPS)

    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        # Verifica se apertou alguma tecla.
        if event.type == pygame.KEYDOWN:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx -= 8
            if event.key == pygame.K_RIGHT:
                player.speedx += 8
            if event.key == pygame.K_SPACE:
                player.shoot()
        # Verifica se soltou alguma tecla.
        if event.type == pygame.KEYUP:
            # Dependendo da tecla, altera a velocidade.
            if event.key == pygame.K_LEFT:
                player.speedx += 8
            if event.key == pygame.K_RIGHT:
                player.speedx -= 8
