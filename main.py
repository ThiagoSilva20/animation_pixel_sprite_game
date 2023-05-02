import pygame 
from pygame.locals import *
from sys import exit

pygame.init()

largura = 640
altura = 480

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Sprites')

preto = (0,0,0)

class Personagem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
    	
        self.sprites.append(pygame.image.load('pixel_game/T_academia/sprite_0.png'))
    	
        self.sprites.append(pygame.image.load('pixel_game/T_academia/sprite_1.png'))
    	
        self.sprites.append(pygame.image.load('pixel_game/T_academia/sprite_2.png'))   
        
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (32*6, 32*6))
        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 100
        self.animar = False

    def atacar(self):
        self.animar = True
    def update(self):
        if self.animar == True:
            self.atual = self.atual + 0.5
            if self.atual >= len(self.sprites):
                self.atual = 0
                self.animar = False
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (32*6, 32*6))


todas_as_sprites = pygame.sprite.Group()
personagem = Personagem()
todas_as_sprites.add(personagem)

relogio = pygame.time.Clock()   
while True:
    relogio.tick(30)
    tela.fill(preto)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            personagem.atacar()
    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    pygame.display.flip()
