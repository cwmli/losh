import pygame,os
#Brick Block
class brick(pygame.sprite.Sprite):
    def __init__(self, g_x, g_y):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(os.path.join('resources',"brick.png"))
        
        self.rect = self.image.get_rect()
        self.rect.x = g_x
        self.rect.y = g_y
#Transition Block Right
class trbr(pygame.sprite.Sprite):
    def __init__(self, tr1_x, tr1_y):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(os.path.join('resources',"brick_r.png"))
        
        self.rect = self.image.get_rect()
        self.rect.x = tr1_x
        self.rect.y = tr1_y
#Transition Block Left
class trbl(pygame.sprite.Sprite):
    def __init__(self, tr_x, tr_y):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.transform.flip(pygame.image.load(os.path.join('resources',"brick_r.png")), True,False)

        
        self.rect = self.image.get_rect()
        self.rect.x = tr_x
        self.rect.y = tr_y
#Platform
class b_platform(pygame.sprite.Sprite):
    def __init__ (self, bp_x, bp_y):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load(os.path.join('resources',"brick.png"))

        self.rect = self.image.get_rect()
        self.rect.x = bp_x
        self.rect.y = bp_y
