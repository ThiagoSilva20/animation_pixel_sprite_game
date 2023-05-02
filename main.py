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
    	
        self.sprites.append(pygame.image.load('T_academia/sprite_0.png'))
    	
        self.sprites.append(pygame.image.load('T_academia/sprite_1.png'))
    	
        self.sprites.append(pygame.image.load('T_academia/sprite_2.png'))   
        
        self.atual = 0
        self.image = self.sprites[self.atual]
        self.image = pygame.transform.scale(self.image, (32*2, 32*2))
        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 220
        

    def update(self):
            self.atual = self.atual + 0.5
            if self.atual >= len(self.sprites):
                self.atual = 0
            self.image = self.sprites[int(self.atual)]
            self.image = pygame.transform.scale(self.image, (32*2, 32*2))


todas_as_sprites = pygame.sprite.Group()
personagem = Personagem()
todas_as_sprites.add(personagem)

imagem_fundo = pygame.image.load('T_academia/back_image.jpg').convert()
imagem_fundo = pygame.transform.scale(imagem_fundo, (640, 480))

relogio = pygame.time.Clock()   
while True:
    relogio.tick(30)
    tela.fill(preto)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    tela.blit(imagem_fundo, (0,0))
    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    pygame.display.flip()
