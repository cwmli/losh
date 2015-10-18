import pygame,os,blockdata,spritestor,fontdata,colordata

mtblock_list = pygame.sprite.Group()

mtplatforms = pygame.sprite.Group()

mtall_sprites_list = pygame.sprite.Group()

door1 = pygame.image.load(os.path.join('resources',"door1.png"))

def create_level(mtblock_list,mtall_sprites_list,mtplatforms):
#---LEVEL---#
    #---bottom platforms---#
    for bp_x in range(50,600,50):
        bp_y = 550
        platblock = blockdata.b_platform(bp_x,bp_y)
        mtplatforms.add(platblock)
        mtall_sprites_list.add(platblock)
    transblockr = blockdata.trbr(600,550)
    mtplatforms.add(transblockr)
    mtall_sprites_list.add(transblockr)
    #---second level platforms---#
    #---right side---#
    for bp_x in range(650,850,50):
        bp_y = 350
        platblock = blockdata.b_platform(bp_x,bp_y)
        mtplatforms.add(platblock)
        mtall_sprites_list.add(platblock)
    transblockl = blockdata.trbl(600,350)
    mtplatforms.add(transblockl)
    mtall_sprites_list.add(transblockl)
    #---left side---#
    transblockr = blockdata.trbr(50,350)
    mtplatforms.add(transblockr)
    mtall_sprites_list.add(transblockr)
#---------------------------------------------------------------------------#      
    #---Left BLOCK BORDER---#
    for g_y in range(0,600,50):
        g_x = 0
        brickblock = blockdata.brick(g_x,g_y)
        mtblock_list.add(brickblock)
        mtall_sprites_list.add(brickblock)
    #---Right BLOCK BORDER---#
    for g_y in range(0,600,50):
        g_x = 850
        brickblock = blockdata.brick(g_x,g_y)
        mtblock_list.add(brickblock)
        mtall_sprites_list.add(brickblock)
#---------------------------------------------------------------------------#
spritestor.block_list.add(mtblock_list)
spritestor.platforms.add(mtplatforms)
spritestor.all_sprites_list.add(mtall_sprites_list)
