import pygame,random,os,time,math,spritestor,fontdata,maptutorial,maplboss,mapl1,mapl2,mapl3,colordata
# Player 1
class player(pygame.sprite.Sprite):
    global c_x,c_y,invuln,invulntimer,pwrgain,hatpl,holding_weapon,j_time,d_time,master,javail,attackavail,c_yspd,c_xspd,leftavail,rightavail,delay,faceright,faceleft,attacknum,kills
    # start speed
    c_yspd = "stop"
    c_xspd = "stop"
    # jump limit
    javail = True
    rightavail = True
    attackavail = True
    leftavail = True
    faceright = True
    faceleft = False
    invuln = False
    invulntimer = 0
    holding_weapon = False
    j_time = 0
    d_time = 0
    master = True
    pwrgain = 10
    attacknum = 0
    kills = 0
    hatpl = 0
    delay = 0
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.hand = pygame.image.load(os.path.join('resources',"defaulthands.png"))
    
        self.images = []
        self.images.append(pygame.image.load(os.path.join('resources',"character4.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"character5.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"character6.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"character5.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"character4.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"character3.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"character2.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"character3.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"character4.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"character_jump.png")))
        
        self.index = 0
        self.rect = self.images[0].get_rect()
                
    def update(self,group):
        global c_x,c_y,c_yspd,invuln,invulntimer,score,newlev,hatspawned,indicate,master,javail,j_time,d_time,rightavail,leftavail, c_xspd,delay,p_health,faceright,faceleft,randwep,hatpl

        if not holding_weapon and c_yspd != "jump":
            screen.blit(self.hand,(c_x,c_y+25))

        if delay == 5:
            self.index+=1
            delay = 0
        if self.index == 8:
            self.index = 0
        self.image = self.images[self.index]
        
        self.rect.x = c_x
        self.rect.y = c_y

        colgplat = pygame.sprite.spritecollideany(self,spritestor.platforms)
        
        if colgplat:
            redraw_level = True
            if d_time in range(1,10) and c_xspd == "right" and j_time == 0:
                rightavail = False
                master = False
                c_yspd = "grav"
                c_xspd = "stop"
            if d_time in range(1,10) and c_xspd == "left" and j_time == 0:
                leftavail = False
                master = False
                c_yspd = "grav"
                c_xspd = "stop"
            if c_yspd == "grav" and c_xspd == "right" and j_time == 25 and d_time in range(1,60):
                rightavail = False
                master = False
                c_yspd = "grav"
                c_xspd = "stop"
            if c_yspd == "grav" and c_xspd == "left" and j_time == 25 and d_time in range(1,60):
                leftavail = False
                master = False
                j_time = 0
                c_yspd = "grav"
                c_xspd = "stop"
            if c_yspd != "jump":
                c_yspd = "stop"
                j_time = 0
                d_time = 0
                javail = True
            if j_time in range(16,25) and c_xspd == "right":
                rightavail = False
                master = False
                c_yspd = "grav"
                c_xspd = "stop"
            if j_time in range(16,25) and c_xspd == "left":
                leftavail = False
                master = False
                c_yspd = "grav"
                c_xspd = "stop"
            if c_yspd == "jump" and j_time > 4:
                javail = False
                c_yspd = "grav"



        colgsidewall = pygame.sprite.spritecollideany(self,spritestor.block_list)
        if colgsidewall and c_xspd == "left": 
            c_xspd = "stop"
            leftavail = False
        if colgsidewall and c_xspd == "right": 
            c_xspd = "stop"
            rightavail = False
        if not colgsidewall and colgplat and master:
            rightavail = True
            leftavail = True


        if not colgplat:
            master = True

        
        if j_time == 25 or c_y < 0:
            javail = False
            c_yspd = "grav"

        if c_y > 550:
            c_yspd = "grav"
            c_xspd = "stop"
            rightavail = False
            leftavail = False

        damagesmall = pygame.sprite.spritecollideany(self,spritestor.smallenemies)
        if damagesmall:
            if not invuln:
                p_health -= 1
                invuln = True
        damagelarge = pygame.sprite.spritecollideany(self,spritestor.largeenemies)
        if damagelarge:
            if not invuln:
                p_health -= 2
                invuln = True
            if not invuln and largemob.image == largemob.images_fire[largemob.fireindex]:
                p_health -= 3
                invuln = True
        damageboss = pygame.sprite.spritecollideany(self,spritestor.bosstype)
        if damageboss:
            if not invuln:
                p_health -= 1
                invuln = True
        if invuln:
            invulntimer += 1
            if invulntimer in range(0,100,10):
                self.image = pygame.image.load(os.path.join('resources',"character_damaged.png"))
            if invulntimer == 100:
                invuln = False
                invulntimer = 0

        collidehat = pygame.sprite.spritecollideany(self,spritestor.magichat)
        if collidehat:
           hatspawned = False
           indicate = True
           newlev = False
           randwep = random.randrange(1,6)
           score += 1
           hatpl += pwrgain
         
        #Animation extras
        if c_yspd == "jump":
           self.image = self.images[9]

        if c_xspd == "stop":
            self.image = self.images[0]
        if not faceleft and event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            self.images[0] = pygame.transform.flip(self.images[0], True, False)
            self.images[1] = pygame.transform.flip(self.images[1], True, False)
            self.images[2] = pygame.transform.flip(self.images[2], True, False)
            self.images[3] = pygame.transform.flip(self.images[3], True, False)
            self.images[4] = pygame.transform.flip(self.images[4], True, False)
            self.images[5] = pygame.transform.flip(self.images[5], True, False)
            self.images[6] = pygame.transform.flip(self.images[6], True, False)
            self.images[7] = pygame.transform.flip(self.images[7], True, False)
            self.images[8] = pygame.transform.flip(self.images[8], True, False)
            self.images[9] = pygame.transform.flip(self.images[9], True, False)
            faceright = False
            faceleft = True
        if not faceright and event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            self.images[0] = pygame.transform.flip(self.images[0], True, False)
            self.images[1] = pygame.transform.flip(self.images[1], True, False)
            self.images[2] = pygame.transform.flip(self.images[2], True, False)
            self.images[3] = pygame.transform.flip(self.images[3], True, False)
            self.images[4] = pygame.transform.flip(self.images[4], True, False)
            self.images[5] = pygame.transform.flip(self.images[5], True, False)
            self.images[6] = pygame.transform.flip(self.images[6], True, False)
            self.images[7] = pygame.transform.flip(self.images[7], True, False)
            self.images[8] = pygame.transform.flip(self.images[8], True, False)
            self.images[9] = pygame.transform.flip(self.images[9], True, False)
            faceright = True
            faceleft = False
            
    def calc_grav(self):
        global c_y,c_yspd

        if c_y < 600 and c_yspd != "jump":
            c_yspd = "grav"

#----------------------------------------------------------------------------#
class player_life(pygame.sprite.Sprite):
    global p_health
    p_health = 3

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        global p_health,done,gameoverpage,ls1,ls2,ls3,ls4,ls5,freeplay

        self.image = pygame.image.load(os.path.join('resources',"heart.png"))
      
        self.rect = self.image.get_rect()
        self.rect.x = 175

        for i in range(p_health):
            screen.blit(self.image,(self.rect.x, 12))
            screen.blit(fontdata.bit.render("HEALTH:"+" ",1,colordata.black),(60,10))
            self.rect.x += 30

        if p_health <= 0:
            gameoverpage = True
            if ls1:
                ls1 = False
            if ls2:
                ls2 = False
            if ls3:
                ls3 = False
            if ls4:
                ls4 = False
            if ls5:
                ls5 = False
            if freeplay:
                freeplay = False
#-----WEAPONS---------------------------------------------------------------#
class wepselected:
    global randwep,javelin_wep,catcannon_wep,leafblower_wep,watergun_wep,rainbowgun_wep
    randwep = 0
    javelin_wep = False
    catcannon_wep = False
    leafblower_wep = False
    watergun_wep = False
    rainbowgun_wep = False
    
    def __init__(self):
        global catcannon_wep,javelin_wep,holding_weapon,randwep,leafblower_wep,watergun_wep,rainbowgun_wep
        indicateypos = c_y - 50
        if randwep == 1:
            javelin_wep = True
            catcannon_wep = False
            leafblower_wep = False
            watergun_wep = False
            rainbowgun_wep = False
            
            spritestor.onhand.empty()
            spritestor.onhand.add(javelinheld())
            holding_weapon = True
            randwep = 0

        if randwep == 2:
            catcannon_wep = True
            javelin_wep = False
            leafblower_wep = False
            watergun_wep = False
            rainbowgun_wep = False
            
            spritestor.onhand.empty()
            spritestor.onhand.add(catcannon())
            holding_weapon = True
            randwep = 0

        if randwep == 3:
            leafblower_wep = True
            javelin_wep = False
            catcannon_wep = False
            watergun_wep = False
            rainbowgun_wep = False
            
            spritestor.onhand.empty()
            spritestor.onhand.add(leafblower())
            holding_weapon = True
            randwep = 0

        if randwep == 4:
            watergun_wep = True
            leafblower_wep = False
            javelin_wep = False
            catcannon_wep = False
            rainbowgun_wep = False

            spritestor.onhand.empty()
            spritestor.onhand.add(watergun())
            holding_weapon = True
            randwep = 0

        if randwep == 5:
            rainbowgun_wep = True
            leafblower_wep = False
            javelin_wep = False
            catcannon_wep = False
            watergun_wep = False

            spritestor.onhand.empty()
            spritestor.onhand.add(rainbowgun())
            holding_weapon = True
            randwep = 0
            
class wepindicate:
    global indicate,indicatedelay,setpos
    indicate = False
    indicatedelay = 0
    setpos = True
    def __init__(self):
        global indicate,indicatedelay,indicateypos,indicatexpos,setpos
        if setpos:
            indicateypos = hat.rect.y - 75
            indicatexpos = hat.rect.x - 20
            setpos = False
        if indicate:
            if leafblower_wep:
                screen.blit(fontdata.font.render('Leafblower',1,colordata.black),(indicatexpos,indicateypos))
                indicatedelay += 1
                indicateypos -=1
                if indicatedelay == 60:
                    indicatedelay = 0
                    indicate = False
                    setpos = True
            if catcannon_wep:
                screen.blit(fontdata.font.render('Cat Cannon',1,colordata.black),(indicatexpos,indicateypos))
                indicatedelay += 1
                indicateypos -=1
                if indicatedelay == 60:
                    indicatedelay = 0
                    indicate = False
                    setpos = True
            if javelin_wep:
                screen.blit(fontdata.font.render('Javelin',1,colordata.black),(indicatexpos,indicateypos))
                indicatedelay += 1
                indicateypos -=1
                if indicatedelay == 60:
                    indicatedelay = 0
                    indicate = False
                    setpos = True
                    
            if watergun_wep:
                screen.blit(fontdata.font.render('Water Gun',1,colordata.black),(indicatexpos,indicateypos))
                indicatedelay += 1
                indicateypos -=1
                if indicatedelay == 60:
                    indicatedelay = 0
                    indicate = False
                    setpos = True

            if rainbowgun_wep:
                screen.blit(fontdata.font.render('Rainbow Gun',1,colordata.black),(indicatexpos,indicateypos))
                indicatedelay += 1
                indicateypos -=1
                if indicatedelay == 60:
                    indicatedelay = 0
                    indicate = False
                    setpos = True
#-----------------------------------------------------------------------------#
class rainbowgun(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.faceright = True
        self.faceleft = False
        self.offset = -5
        self.images.append(pygame.image.load(os.path.join('resources',"rainbowgun.png")))

        self.rect = self.images[0].get_rect()

    def update(self):
        self.image = self.images[0]
        self.rect.x = c_x - self.offset
        self.rect.y = c_y 

        if not self.faceleft and event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            self.images[0] = pygame.transform.flip(self.images[0],True,False)
            self.offset = 18
            self.faceright = False
            self.faceleft = True
        if not self.faceright and event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            self.images[0] = pygame.transform.flip(self.images[0],True,False)
            self.offset = -5
            self.faceright = True
            self.faceleft = False

class rainbowshot(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        rbs.play()
        self.leftflipped = faceleft
        self.checked = False
        self.images = []
        self.xmove = -7

        self.images.append(pygame.image.load(os.path.join('resources',"rainbowshot.png")))

        self.rect = self.images[0].get_rect()
        self.rect.x = c_x 
        self.rect.y = c_y + 20

    def update(self):
        global attackavail

        self.image = self.images[0]

        self.rect.x += self.xmove
        
        if not self.checked:
            if not self.leftflipped  and not faceleft:
                self.images[0] = pygame.transform.flip(self.images[0],True,False)
                self.leftflipped = True
                self.xmove = 7

        block = pygame.sprite.spritecollideany(self,spritestor.block_list)
        platform = pygame.sprite.spritecollideany(self,spritestor.platforms)
        if block or platform:
            self.kill()
            attackavail = True
#-----------------------------------------------------------------------------#
class watergun(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.faceright = True
        self.faceleft = False
        self.offset = 6
        self.images.append(pygame.image.load(os.path.join('resources',"watergun.png")))

        self.rect = self.images[0].get_rect()

    def update(self):
        self.image = self.images[0]
        self.rect.x = c_x - self.offset
        self.rect.y = c_y 

        if not self.faceleft and event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            self.images[0] = pygame.transform.flip(self.images[0],True,False)
            self.offset = 10
            self.faceright = False
            self.faceleft = True
        if not self.faceright and event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            self.images[0] = pygame.transform.flip(self.images[0],True,False)
            self.offset = 6
            self.faceright = True
            self.faceleft = False

class water(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.leftflipped = faceleft
        self.checked = False
        self.images = []
        self.xmove = -7

        self.images.append(pygame.image.load(os.path.join('resources',"watershot.png")))

        self.rect = self.images[0].get_rect()
        self.rect.x = c_x 
        self.rect.y = c_y + 20

    def update(self):
        global attackavail,waterxpos,waterypos,waterxmove
        waterxmove = self.xmove
        waterxpos = self.rect.x
        waterypos = self.rect.y
        self.image = self.images[0]

        self.rect.x += self.xmove
        
        if not self.checked:
            if not self.leftflipped  and not faceleft:
                self.images[0] = pygame.transform.flip(self.images[0],True,False)
                self.leftflipped = True
                self.xmove = 7

        block = pygame.sprite.spritecollideany(self,spritestor.block_list)
        platform = pygame.sprite.spritecollideany(self,spritestor.platforms)
        if block or platform:
            self.kill()
            spritestor.projectile_effects.add(wsplash())
            attackavail = True
#-----------------------------------------------------------------------------#
class leafblower(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.faceright = True
        self.faceleft = False
        self.offset = 16
        self.images.append(pygame.image.load(os.path.join('resources',"leafblower.png")))

        self.rect = self.images[0].get_rect()

    def update(self):
        self.image = self.images[0]
        self.rect.x = c_x - self.offset
        self.rect.y = c_y 

        if not self.faceleft and event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            self.images[0] = pygame.transform.flip(self.images[0],True,False)
            self.offset = 16
            self.faceright = False
            self.faceleft = True
        if not self.faceright and event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            self.images[0] = pygame.transform.flip(self.images[0],True,False)
            self.offset = 16
            self.faceright = True
            self.faceleft = False

class blow(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.checked = False
        self.leftflipped = faceleft
        self.offset = 120
        self.blowdelay = 0
        self.blow_i = 0
        
        self.images = []
        self.images.append(pygame.image.load(os.path.join('resources',"blow.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"blow1.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"blow2.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"blow3.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"blow4.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"blow5.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"blow6.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"blow7.png")))

        self.rect = self.images[0].get_rect()

    def update(self):
        global attackavail
        self.image = self.images[self.blow_i]
        self.rect.x = c_x - self.offset
        self.rect.y = c_y - 5
        
        if not self.checked:
            if not self.leftflipped  and not faceleft:
                self.images[0] = pygame.transform.flip(self.images[0],True,False)
                self.images[1] = pygame.transform.flip(self.images[1],True,False)
                self.images[2] = pygame.transform.flip(self.images[2],True,False)
                self.images[3] = pygame.transform.flip(self.images[3],True,False)
                self.images[4] = pygame.transform.flip(self.images[4],True,False)
                self.images[5] = pygame.transform.flip(self.images[5],True,False)
                self.images[6] = pygame.transform.flip(self.images[6],True,False)
                self.images[7] = pygame.transform.flip(self.images[7],True,False)
                self.offset = -50
                self.leftflipped = True


        self.blowdelay += 1
        if self.blowdelay == 7:
            self.blow_i += 1
            self.blowdelay = 0
        if self.blow_i >= len(self.images):
            self.kill()
            attackavail = True

        
#-----------------------------------------------------------------------------#
class javelinheld(pygame.sprite.Sprite):
   
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.faceright = True
        self.faceleft = False
        self.offset = 16
        self.images.append(pygame.image.load(os.path.join('resources',"javelinheld.png")))

        self.rect = self.images[0].get_rect()


    def update(self):
        self.image = self.images[0]
        self.rect.x = c_x - self.offset
        self.rect.y = c_y 

        if not self.faceleft and event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            self.images[0] = pygame.transform.flip(self.images[0],True,False)
            self.offset = 16
            self.faceright = False
            self.faceleft = True
        if not self.faceright and event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            self.images[0] = pygame.transform.flip(self.images[0],True,False)
            self.offset = 16
            self.faceright = True
            self.faceleft = False
            
class javelin(pygame.sprite.Sprite):
    
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        jav.play()
        self.leftflipped = faceleft
        self.checked = False
        self.images = []
        self.xmove = -5

        self.images.append(pygame.image.load(os.path.join('resources',"javelin.png")))

        self.rect = self.images[0].get_rect()
        self.rect.x = c_x
        self.rect.y = c_y + 20

    def update(self):
        global attackavail
        self.image = self.images[0]

        self.rect.x += self.xmove
        
        if not self.checked:
            if not self.leftflipped  and not faceleft:
                self.images[0] = pygame.transform.flip(self.images[0],True,False)
                self.leftflipped = True
                self.xmove = 5

        block = pygame.sprite.spritecollideany(self,spritestor.block_list)
        platform = pygame.sprite.spritecollideany(self,spritestor.platforms)
        if block or platform:
            self.kill()
            attackavail = True
#-----------------------------------------------------------------------------#
class catcannon(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.faceright = True
        self.faceleft = False
        self.offset = 6
        self.images.append(pygame.image.load(os.path.join('resources',"catcannon.png")))

        self.rect = self.images[0].get_rect()


    def update(self):
        global attackavail
        self.image = self.images[0]
        self.rect.x = c_x - self.offset
        self.rect.y = c_y 

        if not self.faceleft and event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
            self.images[0] = pygame.transform.flip(self.images[0],True,False)
            self.offset = 26
            self.faceright = False
            self.faceleft = True
        if not self.faceright and event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
            self.images[0] = pygame.transform.flip(self.images[0],True,False)
            self.offset = 6
            self.faceright = True
            self.faceleft = False

class catshot(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.leftflipped = faceleft
        self.checked = False
        self.images = []
        self.xmove = -10

        self.images.append(pygame.image.load(os.path.join('resources',"catball.png")))

        self.rect = self.images[0].get_rect()
        self.rect.x = c_x 
        self.rect.y = c_y + 20

    def update(self):
        global attackavail,catshotxpos,catshotypos
        catshotxpos = self.rect.x
        catshotypos = self.rect.y
        self.image = self.images[0]

        self.rect.x += self.xmove
        
        if not self.checked:
            if not self.leftflipped  and not faceleft:
                self.images[0] = pygame.transform.flip(self.images[0],True,False)
                self.leftflipped = True
                self.xmove = 10

        block = pygame.sprite.spritecollideany(self,spritestor.block_list)
        platform = pygame.sprite.spritecollideany(self,spritestor.platforms)
        if block or platform:
            self.kill()
            spritestor.projectile_effects.add(explosion())
            attackavail = True
#----------------------------------------------------------##!#!#
class bossshot(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        lsblt.play()
        self.leftflipped = bossfaceleft
        self.checked = False
        self.images = []
        self.xmove = 10

        self.images.append(pygame.image.load(os.path.join('resources',"rbbeam.png")))

        self.rect = self.images[0].get_rect()
        self.image = self.images[0]
        self.rect.x = bossx
        self.rect.y = bossy + 10

    def update(self):
        global attackavail,bossshotx,bossshoty
        bossshotx = self.rect.x
        bossshoty = self.rect.y
        self.rect.x += self.xmove
        
        if not self.checked:
            if self.leftflipped:
                self.leftflipped = True
                self.xmove = -10

        block = pygame.sprite.spritecollideany(self,spritestor.block_list)
        platform = pygame.sprite.spritecollideany(self,spritestor.platforms)
        if block or platform:
            self.kill()
            spritestor.projectile_effects.add(bexplosion())
class bexplosion(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        xplos.play()

        self.images = []
        self.images.append(pygame.image.load(os.path.join('resources',"xplosion.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"xplosion1.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"xplosion2.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"xplosion3.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"xplosion4.png")))

        self.rect = self.images[0].get_rect()
        self.rect.x = bossshotx - 40
        self.rect.y = bossshoty - 40

        self.xplo_i = 0
        self.xplodelay = 0
    def update(self):
        self.image = self.images[self.xplo_i]

        self.xplodelay += 1
        if self.xplodelay == 10:
            self.xplo_i += 1
            self.xplodelay = 0
        if self.xplo_i >= len(self.images):
            self.kill()
#----------------WEAPON EFFECTS-----------------------------------------------#
class explosion(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        xplos.play()

        self.images = []
        self.images.append(pygame.image.load(os.path.join('resources',"xplosion.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"xplosion1.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"xplosion2.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"xplosion3.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"xplosion4.png")))

        self.rect = self.images[0].get_rect()
        self.rect.x = catshotxpos - 40
        self.rect.y = catshotypos - 40

        self.xplo_i = 0
        self.xplodelay = 0
    def update(self):
        self.image = self.images[self.xplo_i]

        self.xplodelay += 1
        if self.xplodelay == 10:
            self.xplo_i += 1
            self.xplodelay = 0
        if self.xplo_i >= len(self.images):
            self.kill()
class shotsmoke(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.checked = False
        self.leftflipped = faceleft

        self.images = []
        self.images.append(pygame.image.load(os.path.join('resources',"xplosion3.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"xplosion4.png")))
        self.rect = self.images[0].get_rect()
        self.rect.x = c_x - 100
        self.rect.y = c_y - 20

        self.smoke_i = 0
        self.smokedelay = 0
        if not self.checked:
            if not self.leftflipped  and not faceleft:
                self.leftflipped = True
                self.rect.x = c_x + 10
    def update(self):
        self.image = self.images[self.smoke_i]
        
        self.smokedelay += 1
        if self.smokedelay == 7:
            self.smoke_i += 1
            self.smokedelay = 0
        if self.smoke_i >= len(self.images):
            self.kill()

class wsplash(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.images = []
        self.images.append(pygame.image.load(os.path.join('resources',"wsplash.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"wsplash1.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"wsplash2.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"wsplash3.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"wsplash4.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"wsplash5.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"wsplash6.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"wsplash7.png")))

        self.rect = self.images[0].get_rect()
        self.rect.x = waterxpos 
        self.rect.y = waterypos - 20

        if waterxmove == 7:
            self.rect.x = waterxpos + 40
            self.images[0] = pygame.transform.flip(self.images[0],True,False)
            self.images[1] = pygame.transform.flip(self.images[1],True,False)
            self.images[2] = pygame.transform.flip(self.images[2],True,False)
            self.images[3] = pygame.transform.flip(self.images[3],True,False)
            self.images[4] = pygame.transform.flip(self.images[4],True,False)
            self.images[5] = pygame.transform.flip(self.images[5],True,False)
            self.images[6] = pygame.transform.flip(self.images[6],True,False)
            self.images[7] = pygame.transform.flip(self.images[7],True,False)
            
        self.wsp_i = 0
        self.wspdelay = 0
    def update(self):
        self.image = self.images[self.wsp_i]

        self.wspdelay += 1
        if self.wspdelay == 3:
            self.wsp_i += 1
            self.wspdelay = 0
        if self.wsp_i >= len(self.images):
            self.kill()

#-----------------------------------------------------------------------------#
class hat(pygame.sprite.Sprite):
    global hatspawned,randspawn,newlev
    hatspawned = False
    randspawn = 0
    newlev = True

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.image.load(os.path.join('resources',"hat.png"))
        self.rect = self.image.get_rect()

    def update(self):
        global randspawn,hatspawned
        
        if not hatspawned:
            randspawn = random.randrange(1,5)
            hatspawned = True

        if newlev:
             self.rect.x = 425
             self.rect.y = 250

        if ls1 or ls3 or ls4 or ls5 or freeplay:    
            if randspawn == 1:
                self.rect.x = random.randrange(250,630)
                self.rect.y = 120
                randspawn = 0
            if randspawn == 2:
                self.rect.x = random.randrange(650,830)
                self.rect.y = 320
                randspawn = 0
            if randspawn == 3:
                self.rect.x = random.randrange(50,230)
                self.rect.y = 320
                randspawn = 0
            if randspawn == 4:
                self.rect.x = random.randrange(250,630)
                self.rect.y = 520
                randspawn = 0            
        if ls2:
            if randspawn == 1:
                self.rect.x = random.randrange(50,230)
                self.rect.y = 120
                randspawn = 0
            if randspawn == 2:
                self.rect.x = random.randrange(650,830)
                self.rect.y = 120
                randspawn = 0
            if randspawn == 3:
                self.rect.x = random.randrange(50,230)
                self.rect.y = 520
                randspawn = 0
            if randspawn == 4:
                self.rect.x = random.randrange(650,830)
                self.rect.y = 520
                randspawn = 0

#---BOSS-----------------------------------------------------------------------#
class boss(pygame.sprite.Sprite):
    global stopped,tooclose,stoptime,xdist,followx,followy,attackchoice,bossfaceleft
    stopped = False
    stoptime = 0
    attackchoice = 0
    tooclose = False
    xdist = 90
    followx = True
    followy = True
    bossfaceleft = False

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.attackdelay = 0
        self.attacktime = 200
        self.attackchoicedelay = 0
        self.health = 250
        
        self.images_r = []
        self.images_l = []

        self.images_r.append(pygame.image.load(os.path.join('resources',"boss4.png")))
        self.images_r.append(pygame.image.load(os.path.join('resources',"boss5.png")))
        
        self.images_l.append(pygame.image.load(os.path.join('resources',"boss2.png")))
        self.images_l.append(pygame.image.load(os.path.join('resources',"boss3.png")))

        self.rect = self.images_r[0].get_rect()

        
    def update(self):
        global bossmx,bossmy,bossx,bossy,stopped,stoptime,tooclose,followx,xdist,attackchoice,attackavail,bossfaceleft,gamefinish
        (bossmx,bossmy) = ((c_x - self.rect.x)/math.sqrt((c_x - self.rect.x) ** 2 + (c_y - self.rect.y) ** 2), 
                        (c_y - self.rect.y)/math.sqrt((c_x - self.rect.x) ** 2 + (c_y - self.rect.y) ** 2))
        bossx = self.rect.x
        bossy = self.rect.y

        if not stopped:
            if followx:
                self.rect.x += bossmx*5
            if followy:
                self.rect.y += bossmy*3
       
        if self.rect.y - c_y < 5 and self.rect.x - c_x in range(-xdist,xdist):
            tooclose = True

        if tooclose:
            stopped = True
            stoptime += 1
            if stoptime == 50:
                stopped = False
                tooclose = False
                stoptime = 0

        #attack        
        self.attackdelay += 1
        if self.attackdelay == self.attacktime:
            attackchoice = random.randrange(1,4)
            followx = False
            self.attackdelay = 0

        if self.attackdelay > self.attacktime:
            self.attackdelay = 0

        if attackchoice == 1:
            #add flying mob that chases player
            if self.attackchoicedelay == 60:
                followx = True
                self.attackchoicedelay = 0
                self.attackchoice = 0

        if attackchoice == 2:
            self.attackchoicedelay += 1
            spritestor.bosstype.add(bossshot())
            if self.attackchoicedelay == 20:
                followx = True
                self.attackchoicedelay = 0
                self.attackchoice = 0

        if attackchoice == 3:
            self.attackchoicedelay += 1
            xdist = 20
            followx = True
            if self.attackchoicedelay == 100:
                xdist = 90
                self.attackdchoicedelay = 0
                self.attackchoice = 0

        #damage take
        colglowdmg = pygame.sprite.spritecollideany(self,spritestor.projectile_lowdmg)
        colgmeddmg = pygame.sprite.spritecollideany(self,spritestor.projectile_meddmg)
        colghighdmg = pygame.sprite.spritecollideany(self,spritestor.projectile_highdmg)
        if colghighdmg:
            self.health -= 0.5
            attackavail = True
        if colgmeddmg:
            self.health -= 5
            spritestor.projectile_meddmg.empty()
            if catcannon_wep:
                spritestor.projectile_effects.add(explosion())
            if watergun_wep:
                spritestor.projectile_effects.add(wsplash())
            attackavail = True
        if colglowdmg:
            self.health -= 4
            spritestor.projectile_lowdmg.empty()
            attackavail = True

        if self.health <= 0:
            self.kill()
            gamefinish = True

        #sprite face direction
        if bossmx*5 > 0:
            self.image = self.images_r[1]
            bossfaceleft = False
        if bossmx*5 < 0:
            self.image = self.images_l[0]
            bossfaceleft = True
        if bossmx*5 == 0:
            if self.image == self.images_l[0]:
                self.image = self.images_l[1]
                bossfaceleft = True
            if self.image == self.images_r[1]:
                self.image = self.images_r[0]
                bossfaceleft = False
#---MONSTERS-------------------------------------------------------------------#
class mob(pygame.sprite.Sprite):
    global mfspd,mdelay,timebetween,aggrav,normal,mob_health,spawningsmall
    normal = True
    aggrav = False
    mob_health = 5
    mfspd = 7
    timebetween = 7
    mdelay = 0
    
    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)
        self.aggrav = aggrav
        self.normal = normal
        self.mspd = 3
        self.mfspd = mfspd
        self.timebetween = timebetween
        self.mdelay = mdelay
        self.mhealth = mob_health
        
        self.images_n = []
        self.images_a = []

        self.images_n.append(pygame.image.load(os.path.join('resources',"monster3.png")))
        self.images_n.append(pygame.image.load(os.path.join('resources',"monster4.png")))
        self.images_n.append(pygame.image.load(os.path.join('resources',"monster5.png")))
        self.images_n.append(pygame.image.load(os.path.join('resources',"monster4.png")))
        self.images_n.append(pygame.image.load(os.path.join('resources',"monster3.png")))
        self.images_n.append(pygame.image.load(os.path.join('resources',"monster2.png")))
        self.images_n.append(pygame.image.load(os.path.join('resources',"monster1.png")))
        self.images_n.append(pygame.image.load(os.path.join('resources',"monster2.png")))
        
        self.images_a.append(pygame.image.load(os.path.join('resources',"monster_a3.png")))
        self.images_a.append(pygame.image.load(os.path.join('resources',"monster_a4.png")))
        self.images_a.append(pygame.image.load(os.path.join('resources',"monster_a5.png")))
        self.images_a.append(pygame.image.load(os.path.join('resources',"monster_a4.png")))
        self.images_a.append(pygame.image.load(os.path.join('resources',"monster_a3.png")))
        self.images_a.append(pygame.image.load(os.path.join('resources',"monster_a2.png")))
        self.images_a.append(pygame.image.load(os.path.join('resources',"monster_a1.png")))
        self.images_a.append(pygame.image.load(os.path.join('resources',"monster_a2.png")))
        
        self.index = 0
        self.rect = self.images_n[0].get_rect()
        self.rect.move_ip(425,random.randint(0,10))
        if ls2:
            self.rect.x = 625
            self.rect.y = 0
                             
    def update(self,group):
        global attackavail,spawnedsmall,kills
        self.mdelay += 1
        self.rect.move_ip(self.mspd,self.mfspd)
        if self.mdelay >= self.timebetween:
            self.index+=1
            self.mdelay = 0
        if self.index >= len(self.images_n):
            self.index = 0
        if self.normal:
            self.image = self.images_n[self.index]
        if self.aggrav:
            self.image = self.images_a[self.index]
        colgplat = pygame.sprite.spritecollideany(self,spritestor.platforms)
        if colgplat:
            self.mfspd = 0
        if not colgplat:
            self.mfspd = 9
        colgsidewall = pygame.sprite.spritecollideany(self,spritestor.block_list)
        if colgsidewall:
            self.mspd *= -1
            self.images_n[0] = pygame.transform.flip(self.images_n[0],True,False)
            self.images_n[1] = pygame.transform.flip(self.images_n[1],True,False)
            self.images_n[2] = pygame.transform.flip(self.images_n[2],True,False)
            self.images_n[3] = pygame.transform.flip(self.images_n[3],True,False)
            self.images_n[4] = pygame.transform.flip(self.images_n[4],True,False)
            self.images_n[5] = pygame.transform.flip(self.images_n[5],True,False)
            self.images_n[6] = pygame.transform.flip(self.images_n[6],True,False)
            self.images_n[7] = pygame.transform.flip(self.images_n[7],True,False)
            
            self.images_a[0] = pygame.transform.flip(self.images_a[0],True,False)
            self.images_a[1] = pygame.transform.flip(self.images_a[1],True,False)
            self.images_a[2] = pygame.transform.flip(self.images_a[2],True,False)
            self.images_a[3] = pygame.transform.flip(self.images_a[3],True,False)
            self.images_a[4] = pygame.transform.flip(self.images_a[4],True,False)
            self.images_a[5] = pygame.transform.flip(self.images_a[5],True,False)
            self.images_a[6] = pygame.transform.flip(self.images_a[6],True,False)
            self.images_a[7] = pygame.transform.flip(self.images_a[7],True,False)

        if self.rect.y > 550:
            self.aggrav = True
            self.normal = False
            if self.mspd == -3:
                self.mspd = -5
            if self.mspd == 3:
                self.mspd = 5
            self.timebetween = 3
            self.rect.x = 425
            self.rect.y = 0
            if ls2:
                self.rect.x = 280
                self.rect.y = 0


        colglowdmg = pygame.sprite.spritecollideany(self,spritestor.projectile_lowdmg)
        colgmeddmg = pygame.sprite.spritecollideany(self,spritestor.projectile_meddmg)
        colghighdmg = pygame.sprite.spritecollideany(self,spritestor.projectile_highdmg)
        if colghighdmg:
            self.mhealth -= 1
            if self.mspd == -3 or self.mspd == -5:
                self.rect.x += 2
            elif self.mspd == 3 or self.mspd == 5:
                self.rect.x -= 2
            attackavail = True
        if colgmeddmg:
            self.mhealth -= 5
            spritestor.projectile_meddmg.empty()
            if catcannon_wep:
                spritestor.projectile_effects.add(explosion())
            if watergun_wep:
                spritestor.projectile_effects.add(wsplash())
            attackavail = True
        if colglowdmg:
            self.mhealth -= 4
            spritestor.projectile_lowdmg.empty()
            attackavail = True
        if self.mhealth <= 0:
            self.kill()
            spawnedsmall -= 1
            kills += 1
#------------------------------------------------------------------------------#
class largemob(pygame.sprite.Sprite):
    global mlfspd,mldelay,mltimebetween,mlaggrav,mlnormal,mlhealth,spawninglarge
    mlnormal = True
    mlaggrav = False
    mlfspd = 8
    mlhealth = 10
    mltimebetween = 7
    mldelay = 0
    
    def __init__(self,screen):
        pygame.sprite.Sprite.__init__(self)
        global mlfspd,mldelay,mltimebetween,mlaggrav,mlnormal,mlhealth
        self.mlaggrav = mlaggrav
        self.mlnormal = mlnormal
        self.mlspd = 2
        self.mlfspd = mlfspd
        self.mltimebetween = mltimebetween
        self.mldelay = mldelay
        self.mlhealth = mlhealth
        
        self.images_n = []
        self.images_a = []
        self.images_fire = []

        self.images_n.append(pygame.image.load(os.path.join('resources',"monsterl3.png")))
        self.images_n.append(pygame.image.load(os.path.join('resources',"monsterl4.png")))
        self.images_n.append(pygame.image.load(os.path.join('resources',"monsterl5.png")))
        self.images_n.append(pygame.image.load(os.path.join('resources',"monsterl4.png")))
        self.images_n.append(pygame.image.load(os.path.join('resources',"monsterl3.png")))
        self.images_n.append(pygame.image.load(os.path.join('resources',"monsterl2.png")))
        self.images_n.append(pygame.image.load(os.path.join('resources',"monsterl1.png")))
        self.images_n.append(pygame.image.load(os.path.join('resources',"monsterl2.png")))

        self.images_a.append(pygame.image.load(os.path.join('resources',"monsterl_a3.png")))
        self.images_a.append(pygame.image.load(os.path.join('resources',"monsterl_a4.png")))
        self.images_a.append(pygame.image.load(os.path.join('resources',"monsterl_a5.png")))
        self.images_a.append(pygame.image.load(os.path.join('resources',"monsterl_a4.png")))
        self.images_a.append(pygame.image.load(os.path.join('resources',"monsterl_a3.png")))
        self.images_a.append(pygame.image.load(os.path.join('resources',"monsterl_a2.png")))
        self.images_a.append(pygame.image.load(os.path.join('resources',"monsterl_a1.png")))
        self.images_a.append(pygame.image.load(os.path.join('resources',"monsterl_a2.png")))

        self.images_fire.append(pygame.image.load(os.path.join('resources',"monsterlbfire1.png")))
        self.images_fire.append(pygame.image.load(os.path.join('resources',"monsterlbfire2.png")))
        
        self.index = 0
        self.fireindex = 0
        self.fireball = 0
        self.rect = self.images_n[0].get_rect()
        self.rect.move_ip(425,random.randint(0,10))
        if ls2:
            self.rect.x = 625
            self.rect.y = 0
                         
    def update(self,group):
        global spawnedlarge,attackavail,kills
        self.mldelay += 1

        self.fireball += 1

        self.rect.move_ip(self.mlspd,self.mlfspd)
        if self.mldelay >= self.mltimebetween:
            self.index+=1
            self.mldelay = 0
        if self.index >= len(self.images_n):
            self.index = 0
        if self.mlnormal:
            self.image = self.images_n[self.index]
        if self.mlaggrav:
            self.image = self.images_a[self.index]

        if self.fireball >= 5:
            self.fireindex += 1
            self.fireball = 0
        if self.fireindex >= len(self.images_fire):
            self.fireindex = 0
        if self.rect.y - c_y < 10 and self.rect.x - c_x < 70:
            self.image = self.images_fire[self.fireindex]

        colgplat = pygame.sprite.spritecollideany(self,spritestor.platforms)
        if colgplat:
            self.mlfspd = 0
        if not colgplat:
            self.mlfspd = 10
        colgsidewall = pygame.sprite.spritecollideany(self,spritestor.block_list)
        if colgsidewall:
            self.mlspd *= -1
            self.images_n[0] = pygame.transform.flip(self.images_n[0],True,False)
            self.images_n[1] = pygame.transform.flip(self.images_n[1],True,False)
            self.images_n[2] = pygame.transform.flip(self.images_n[2],True,False)
            self.images_n[3] = pygame.transform.flip(self.images_n[3],True,False)
            self.images_n[4] = pygame.transform.flip(self.images_n[4],True,False)
            self.images_n[5] = pygame.transform.flip(self.images_n[5],True,False)
            self.images_n[6] = pygame.transform.flip(self.images_n[6],True,False)
            self.images_n[7] = pygame.transform.flip(self.images_n[7],True,False)

            self.images_a[0] = pygame.transform.flip(self.images_a[0],True,False)
            self.images_a[1] = pygame.transform.flip(self.images_a[1],True,False)
            self.images_a[2] = pygame.transform.flip(self.images_a[2],True,False)
            self.images_a[3] = pygame.transform.flip(self.images_a[3],True,False)
            self.images_a[4] = pygame.transform.flip(self.images_a[4],True,False)
            self.images_a[5] = pygame.transform.flip(self.images_a[5],True,False)
            self.images_a[6] = pygame.transform.flip(self.images_a[6],True,False)
            self.images_a[7] = pygame.transform.flip(self.images_a[7],True,False)            

            self.images_fire[0] = pygame.transform.flip(self.images_fire[0],True,False)
            self.images_fire[1] = pygame.transform.flip(self.images_fire[1],True,False)

        if self.rect.y > 500:
            self.mlaggrav = True
            self.mlnormal = False
            if self.mlspd == -2:
                self.mlspd = -4
            if self.mlspd == 2:
                self.mlspd = 4
            self.mltimebetween = 3
            self.rect.x = 425
            self.rect.y = 0
            if ls2:
                self.rect.x = 280
                self.rect.y = 0

        colglowdmg = pygame.sprite.spritecollideany(self,spritestor.projectile_lowdmg)
        colgmeddmg = pygame.sprite.spritecollideany(self,spritestor.projectile_meddmg)
        colghighdmg = pygame.sprite.spritecollideany(self,spritestor.projectile_highdmg)
        if colghighdmg:
            self.mlhealth -= 0.75
            if self.mlspd == -2 or self.mlspd == -4:
                self.rect.x += 1
            elif self.mlspd == 2 or self.mlspd == 4:
                self.rect.x -= 1
            attackavail = True
        if colgmeddmg:
            self.mlhealth -= 5
            spritestor.projectile_meddmg.empty()
            if catcannon_wep:
                spritestor.projectile_effects.add(explosion())
            if watergun_wep:
                spritestor.projectile_effects.add(wsplash())
            attackavail = True
        if colglowdmg:
            self.mlhealth -= 4
            spritestor.projectile_lowdmg.empty()
            attackavail = True
        if self.mlhealth <= 0:
            self.kill()
            spawnedlarge -= 1
            kills += 1
#----GAME MECHANICS-------------------------------------------------------------#
        
class pause:
    global paused,pausedelay,pausing
    paused = pygame.image.load(os.path.join('resources',"paused.png"))
    pausedelay = 0
    pausing = False
    def __init__(self):
        global pausing,pausedelay
        screen.blit(paused,(380,250))
        pausedelay += 1
        if pausedelay == 5:
            pausedelay = 0
            while 1:
                event = pygame.event.wait()
                if event.type == pygame.KEYDOWN and event.key==pygame.K_p:
                    pausing = False
                    break

class reset:
    def __init__(self):
        global c_x,c_y,faceright,faceleft,clearlist,randsmalldelay,randlargedelay
        spritestor.block_list.empty()
        spritestor.all_sprites_list.empty()
        spritestor.platforms.empty()
        spritestor.smallenemies.empty()
        spritestor.largeenemies.empty()
        spritestor.flyingenemies.empty()
        spritestor.all_sprites_list.add(player)
        clearlist = False
        if ls1:
            c_x = 350
            c_y = 300
            mapl1.create_level(spritestor.block_list,spritestor.all_sprites_list,spritestor.platforms)
        if ls2:
            c_x = 425
            c_y = 250
            mapl2.create_level(spritestor.block_list,spritestor.all_sprites_list,spritestor.platforms)
        if ls3:
            c_x = 425
            c_y = 250
            mapl3.create_level(spritestor.block_list,spritestor.all_sprites_list,spritestor.platforms)
        if ls4:
            c_x = 425
            c_y = 250
            mapl1.create_level(spritestor.block_list,spritestor.all_sprites_list,spritestor.platforms)
        if ls5:
            c_x = 425
            c_y = 250
            maplboss.create_level(spritestor.block_list,spritestor.all_sprites_list,spritestor.platforms)
        randsmalldelay = random.randrange(50,120)
        randlargedelay = random.randrange(120,180)

class eventstart:
    def __init__(self):
        global gameoverpage,ls1,ls2,ls3,ls4,ls5,freeplay
        mobspawn()
        
        spritestor.smallenemies.update(spritestor.block_list)
        spritestor.largeenemies.update(spritestor.block_list)
        player.calc_grav()
        player.update(spritestor.block_list)
                
        spritestor.block_list.update()
        spritestor.all_sprites_list.draw(screen)
        
        spritestor.smallenemies.draw(screen)
        spritestor.largeenemies.draw(screen)
        
        spritestor.magichat.update()
        spritestor.magichat.draw(screen)
        
        spritestor.projectile_lowdmg.update()
        spritestor.projectile_lowdmg.draw(screen)
        spritestor.projectile_meddmg.update()
        spritestor.projectile_meddmg.draw(screen)
        spritestor.projectile_highdmg.update()
        spritestor.projectile_highdmg.draw(screen)
        spritestor.projectile_effects.update()
        spritestor.projectile_effects.draw(screen)
        spritestor.onhand.update()
        spritestor.onhand.draw(screen)
        wepselected()
        wepindicate()
        player_life()

        if c_y > 600:
            gameoverpage = True
            if ls1:
                ls1 = False
            if ls2:
                ls2 = False
            if ls3:
                ls3 = False
            if ls4:
                ls4 = False
            if ls5:
                ls5 = False
            if freeplay:
                freeplay = False

class newdoor:
    def __init__(self):
        global spawning,holding_weapon,newlev
        if ls1:
            if hatpl >= 100:
                spawning = False
                spritestor.smallenemies.empty()
                spritestor.largeenemies.empty()
                spritestor.magichat.empty()
                spritestor.onhand.empty()
                holding_weapon = False
                newlev = True
                screen.blit(door1,(425,450))

        if ls2:
            if hatpl >= 100:
                spawning = False
                spritestor.smallenemies.empty()
                spritestor.largeenemies.empty()
                spritestor.magichat.empty()
                spritestor.onhand.empty()
                holding_weapon = False
                newlev = True
                screen.blit(door1,(425,250))

        if ls3:
            if hatpl >= 100:
                spawning = False
                spritestor.smallenemies.empty()
                spritestor.largeenemies.empty()
                spritestor.magichat.empty()
                spritestor.onhand.empty()
                holding_weapon = False
                newlev = True
                screen.blit(door1,(425,450))
        if ls4:
            if hatpl >= 100:
                spawning = False
                spritestor.smallenemies.empty()
                spritestor.largeenemies.empty()
                spritestor.magichat.empty()
                spritestor.onhand.empty()
                holding_weapon = False
                newlev = True
                screen.blit(door1,(425,450))

class newlevel:
    def __init__(self):
        global ssl,sll,ls1,ls2,ls3,ls4,ls5,clearlist,hatpl,pwrgain,spawnedlarge,spawnedsmall,spawning,p_health        
        if ls1:
            if hatpl >= 100:        
                screen.blit(fontdata.font.render("The power of the hats have been used to spawn a door.",1,colordata.black),(150,225))
                if c_x in range(425,475) and c_y in range(450,550):
                    screen.blit(fontdata.fonts16.render("Press the 'E' key to enter the door.",1,colordata.black),(300,400)) 
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                        spawning = True
                        ssl = 3
                        sll = 1
                        hatpl = 0
                        pwrgain = 5
                        p_health += 1
                        spawnedsmall = 0
                        spawnedlarge = 0
                        ls2 = True
                        ls1 = False
                        clearlist = True
                        spritestor.magichat.add(hat)
                        doorcls.play(1)
                        
        if ls2:
            if hatpl >= 100:
                screen.blit(fontdata.font.render("The power of the hats have been used to spawn a door.",1,colordata.black),(150,225))
                if c_x in range(425,475) and c_y in range(250,350):
                    screen.blit(fontdata.fonts16.render("Press the 'E' key to enter the door.",1,colordata.black),(300,200)) 
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                        spawning = True
                        ssl = 4
                        sll = 1
                        hatpl = 0
                        pwrgain = 5
                        p_health += 2
                        spawnedsmall = 0
                        spawnedlarge = 0
                        ls3 = True
                        ls2 = False
                        clearlist = True
                        spritestor.magichat.add(hat)
                        doorcls.play(1)

        if ls3:
            if hatpl >= 100:
                screen.blit(fontdata.font.render("The power of the hats have been used to spawn a door.",1,colordata.black),(150,225))
                if c_x in range(425,475) and c_y in range(450,550):
                    screen.blit(fontdata.fonts16.render("Press the 'E' key to enter the door.",1,colordata.black),(300,400)) 
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                        spawning = True
                        ssl = 5
                        sll = 2
                        hatpl = 0
                        pwrgain = 4
                        p_health += 3
                        spawnedsmall = 0
                        spawnedlarge = 0
                        ls4 = True
                        ls3 = False
                        clearlist = True
                        spritestor.magichat.add(hat)
                        doorcls.play(1)

        if ls4:
            if hatpl >= 100:
                screen.blit(fontdata.font.render("The power of the hats have been used to spawn a door.",1,colordata.black),(150,225))
                if c_x in range(425,475) and c_y in range(450,550):
                    screen.blit(fontdata.fonts16.render("Press the 'E' key to enter the door.",1,colordata.black),(300,400)) 
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                        spawning = True
                        spritestor.bosstype.add(boss())
                        ssl = 0
                        sll = 0
                        p_health += 5
                        spawnedsmall = 0
                        spawnedlarge = 0
                        ls5 = True
                        ls4 = False
                        clearlist = True
                        spritestor.magichat.add(hat)
                        doorcls.play(1)
                        level.fadeout(5)
                        bossfite.play(-1)
            
class eventstart_basic:
    def __init__(self):
        global ls1,ltut,clearlist,faceright,faceleft

        player.calc_grav()
        player.update(spritestor.block_list)
        
        spritestor.block_list.update()
        spritestor.all_sprites_list.draw(screen)

        spritestor.onhand.update()
        spritestor.onhand.draw(screen)
        wepselected()
        player_life()

        if c_x in range(700,750) and c_y in range(250,350):
            screen.blit(fontdata.fonts16.render("Press the 'E' key to enter the door.",1,colordata.black),(525,225)) 
            if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
                doorcls.play(1)
                ls1 = True
                ltut = False
                clearlist = True
            
class mobspawn:
    global spawning,spawning,spawndelay,spawningsmall,spawninglarge,spawnedsmall,spawnedlarge,randsmalldelay,randlargedelay,ssl,sll
    spawning = True
    spawningsmall = True
    spawninglarge = True
    spawnedsmall = 0
    spawnedlarge = 0
    spawndelay = 0
    randsmalldelay = 0
    randlargedelay = 0
    ssl = 2
    sll = 0
    def __init__(self):
        global spawning,spawndelay,spawningsmall,spawninglarge,spawnedsmall,spawnedlarge,ssl,sll
        if spawning:
            spawndelay += 1
            if spawningsmall:
                if spawndelay == randsmalldelay: 
                    spritestor.smallenemies.add(mob(screen))
                    spawnedsmall += 1
            if spawninglarge:
                if spawndelay == randlargedelay:
                    spritestor.largeenemies.add(largemob(screen))
                    spawndelay = 0
                    spawnedlarge += 1
            if spawndelay == 200:
                spawndelay = 0
            
            if spawnedsmall >= ssl:
                spawningsmall = False
            if spawnedlarge >= sll:
                spawninglarge = False
            if spawnedsmall < ssl:
                spawningsmall = True
            if spawnedlarge< sll:
                spawninglarge = True
#----------------MAIN MENU STUFF-----------------------------------------------#
class controlanima_lr(pygame.sprite.Sprite):
    global controlpageon
    controlpageon = False
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.images.append(pygame.image.load(os.path.join('resources',"akeys.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"akeyl.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"akeys.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"akeyl.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"akeys.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"akeyr.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"akeys.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"akeyr.png")))
         
        self.rect = self.images[0].get_rect()
        self.rect.x = 75
        self.rect.y = 130

        self.controldelay_lr = 0
        self.control_lr = 0

    def update(self):
        self.image = self.images[self.control_lr]

        self.controldelay_lr += 1
        if self.controldelay_lr >= 30:
            self.control_lr += 1
            self.controldelay_lr = 0
        if self.control_lr >= len(self.images):
            self.control_lr = 0

class controlanima_jump(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.images.append(pygame.image.load(os.path.join('resources',"skey.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"skeya.png")))

        self.rect = self.images[0].get_rect()
        self.rect.x = 340
        self.rect.y = 211

        self.controldelay_jp = 0
        self.control_jp = 0

    def update(self):
        self.image = self.images[self.control_jp]

        self.controldelay_jp += 1
        if self.controldelay_jp >= 35:
            self.control_jp += 1
            self.controldelay_jp = 0
        if self.control_jp >= len(self.images):
            self.control_jp = 0

class controlanima_shot(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.images.append(pygame.image.load(os.path.join('resources',"ckey.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"ckey1.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"ckey2.png")))
        self.images.append(pygame.image.load(os.path.join('resources',"ckey3.png")))

        self.rect = self.images[0].get_rect()
        self.rect.x = 695
        self.rect.y = 390

        self.controldelay_c = 0
        self.control_c = 0

    def update(self):
        self.image = self.images[self.control_c]

        self.controldelay_c += 1
        if self.controldelay_c == 15:
            self.control_c += 1
            self.controldelay_c = 0
        if self.control_c >= len(self.images):
            self.control_c = 0
        
#------#
pygame.init()

icon = pygame.image.load(os.path.join("icon.png"))
pygame.display.set_icon(icon)
#---SCREEN SIZE---#
size = [900,600]
screen = pygame.display.set_mode(size)
textonscreen = screen
background = pygame.Surface(screen.get_size())
background = background.convert()
#---Title---#
pygame.display.set_caption("Legend of Sir_Hat")
#---LOAD TITLE---#
gname = pygame.image.load(os.path.join('resources',"gname.png"))
#---LOAD SOUND---#
jav = pygame.mixer.Sound(os.path.join('sound',"jav.ogg"))
lsblt = pygame.mixer.Sound(os.path.join('sound',"lserblst.ogg"))
xplos = pygame.mixer.Sound(os.path.join('sound',"xplo.ogg"))
rbs = pygame.mixer.Sound(os.path.join('sound',"rbs.ogg"))
doorcls = pygame.mixer.Sound(os.path.join('sound',"door.ogg"))
level = pygame.mixer.Sound(os.path.join('sound',"lvl.ogg"))
bossfite = pygame.mixer.Sound(os.path.join('sound',"boss.ogg"))
title = pygame.mixer.Sound(os.path.join('sound',"title.ogg"))
title.play(-1)
#---LOAD OTHERS---#
backarrow = pygame.image.load(os.path.join('resources',"backarrow.png"))
controlpage = pygame.image.load(os.path.join('resources',"controlpage.png"))
gameover = pygame.image.load(os.path.join('resources',"gameover.png"))
background = pygame.image.load(os.path.join('resources',"background.png"))
end = pygame.image.load(os.path.join('resources',"end.png"))
intro = pygame.image.load(os.path.join('resources',"intro.png"))
intro1 = pygame.image.load(os.path.join('resources',"intro1.png")) 
#---Debugging---#
debug_on = False
debug = False

#---VARIABLES---#
#Level management
introopen = True
introopen1 = False
ending = False
menu = True
ltut = False
ls1 = False
ls2 = False
ls3 = False
ls4 = False
ls5 = False
redraw_lv = True
freeplay = False
gameoverpage = False
done = False
movement = False
mouse_over = False
statistics = False
clearlist = False
gamefinish = False
gfstatistics = False
up = 7
#doors:
door1 = pygame.image.load(os.path.join('resources',"door1.png"))
#Screen
height = screen.get_height()
width = screen.get_width()
isfullscreen = False
#score
score = 0
contuse = 0
#------#
hat = hat()
spritestor.magichat.add(hat)
#player
player = player()
c_x = 100
c_y = 300
spritestor.all_sprites_list.add(player)

#------#
clock = pygame.time.Clock()

#---LOOP--#
while done == False:
    #---EVENT---#
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_F12:
            debug = True
            hatpl = 100
            if debug_on:
                debug = False
                debug_on = False
        if event.type == pygame.KEYDOWN and event.key == pygame.K_F11:
            pygame.display.set_mode(size,pygame.FULLSCREEN)
            if isfullscreen:
                pygame.display.set_mode(size)
                isfullscreen = False
                break
            isfullscreen = True
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            pausing = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pressed_array = pygame.mouse.get_pressed()
            for index in range(len(pressed_array)):
                if pressed_array[index]:
                    if menu:
                        if index == 0 and mouse_over and mouse_y in range(190,210):
                            menu = False
                            movement = True
                            title.fadeout(5)
                            level.play(-1)
                            ltut = True
                            redraw_lv = True
                        elif index == 0 and mouse_over and mouse_y in range(210,225):
                            menu = False
                            movement = True
                            title.fadeout(5)
                            level.play(-1)
                            freeplay = True
                            redraw_lv = True 
                        elif index == 0 and mouse_over and mouse_y in range(230,245):
                            menu = False
                            controlpageon = True
                            spritestor.controlpage.add(controlanima_lr(),controlanima_jump(),controlanima_shot())
                        elif index == 0 and mouse_over and mouse_y in range(250,265):
                            done = True
                    if controlpageon:
                        if index == 0 and mouse_x in range(5,180) and mouse_y in range(5,25):
                            controlpageon = False
                            menu = True
                            spritestor.controlpage.empty()
                    if gamefinish:
                        if index == 0 and mouse_x in range(380,520) and mouse_y in range(305,335):
                            gamefinish = False
                            gfstatistics = True
                    if gfstatistics:
                        if index == 0 and mouse_x in range(325,570) and mouse_y in range(400,440): 
                            gfstatistics = False
                            ls5 = False
                            ending = True
                    if gameoverpage:
                        if index == 0 and mouse_x in range(380,520) and mouse_y in range(305,335):
                            gameoverpage = False
                            c_y = 250
                            c_x = 425
                            statistics = True
                    if statistics:
                        if index == 0 and mouse_x in range(325,570) and mouse_y in range(400,440):
                            statistics = False
                            gameoverpage = False
                            if ssl == 2 and sll == 0:
                                ls1 = True
                            elif ssl == 3 and sll == 1:
                                ls2 = True
                            elif ssl == 4 and sll == 1:
                                ls3 = True
                            elif ssl == 5 and sll == 2:
                                ls4 = True
                            elif ssl == 0 and sll == 0:
                                ls5 = True
                            elif ssl == 4 and sll == 2:
                                freeplay = True
                                redraw_lv = True
                                c_y = 250
                                c_x = 425
                            reset()
                            spawnedlarge = 0
                            spawnedsmall = 0
                            p_health = 3
                            contuse += 1
                        if index == 0 and mouse_x in range(320,580) and mouse_y in range(500,540):
                            title.play(-1)
                            level.fadeout(5)
                            bossfite.fadeout(5)
                            reset()
                            menu = True
                            ltut = False
                            ls1 = False
                            ls2 = False
                            ls3 = False
                            ls4 = False
                            ls5 = False
                            redraw_lv = True
                            freeplay = False
                            gameoverpage = False
                            done = False
                            movement = False
                            mouse_over = False
                            statistics = False
                            clearlist = False
                            spawning = True
                            spawningsmall = True
                            spawninglarge = True
                            spawnedsmall = 0
                            spawnedlarge = 0
                            spawndelay = 0
                            randsmalldelay = 0
                            randlargedelay = 0
                            ssl = 2
                            sll = 0
                            contuse = 0
                            mlnormal = True
                            mlaggrav = False
                            mlfspd = 8
                            mlhealth = 10
                            mltimebetween = 7
                            mldelay = 0
                            normal = True
                            aggrav = False
                            mob_health = 5
                            mfspd = 7
                            timebetween = 7
                            mdelay = 0
                            stopped = False
                            stoptime = 0
                            attackchoice = 0
                            tooclose = False
                            xdist = 90
                            followx = True
                            followy = True
                            bossfaceleft = False
                            c_yspd = "stop"
                            c_xspd = "stop"
                            javail = True
                            rightavail = True
                            attackavail = True
                            leftavail = True
                            invuln = False
                            invulntimer = 0
                            holding_weapon = False
                            j_time = 0
                            d_time = 0
                            master = True
                            pwrgain = 10
                            attacknum = 0
                            kills = 0
                            hatpl = 0
                            delay = 0
                            indicate = False
                            indicatedelay = 0
                            setpos = True
                            randwep = 0
                            javelin_wep = False
                            catcannon_wep = False
                            leafblower_wep = False
                            watergun_wep = False
                            rainbowgun_wep = False
                            gamefinish = False
                            gfstatistics = False
                            c_x = 100
                            c_y = 300
                            score = 0
                            spritestor.block_list.empty()
                            spritestor.all_sprites_list.empty()
                            spritestor.platforms.empty()
                            spritestor.smallenemies.empty()
                            spritestor.largeenemies.empty()
                            spritestor.flyingenemies.empty()
                            spritestor.onhand.empty()
                            spritestor.all_sprites_list.add(player)
                    if index == 0:
                        print("Left Click at pos:", mouse_x,mouse_y)
                    if index == 1:
                        print("Mouse Wheel Click at pos:", mouse_x,mouse_y)
                    if index == 2:
                        print("Right Click at pos:", mouse_x,mouse_y)
        if movement:
            if attackavail:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_c:
                    attackavail = False
                    if javelin_wep:
                        spritestor.projectile_lowdmg.add(javelin())
                        attacknum += 1
                    if catcannon_wep:
                        spritestor.projectile_meddmg.add(catshot())
                        spritestor.projectile_effects.add(shotsmoke())
                        attacknum += 1
                    if leafblower_wep:
                        spritestor.projectile_highdmg.add(blow())
                        attacknum += 1
                    if watergun_wep:
                        spritestor.projectile_meddmg.add(water())
                        attacknum += 1
                    if rainbowgun_wep:
                        spritestor.projectile_meddmg.add(rainbowshot())
                        attacknum += 1
            if rightavail:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
                    c_xspd = "right"
                elif event.type == pygame.KEYUP:
                    c_xspd = "stop"
                
            if leftavail:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
                    c_xspd = "left"
                elif event.type == pygame.KEYUP:
                    c_xspd = "stop"
            if javail:
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    c_yspd = "jump"
                elif event.type == pygame.KEYUP:
                    c_yspd = "stop"

            
                                      
    #---Menu LOGIC---#
    pos = pygame.mouse.get_pos()
    mouse_x = pos[0]
    mouse_y = pos[1]
    #---selection---#    
    if mouse_x in range(390,500) and mouse_y in range(190,210):
        mouse_over = True
    elif mouse_x in range(390,500) and mouse_y in range(210,225):
        mouse_over = True
    elif mouse_x in range(390,500) and mouse_y in range(230,245):
        mouse_over = True
    elif mouse_x in range(390,500) and mouse_y in range(250,265):
        mouse_over = True
    #controlsele    
    elif mouse_x in range(5,180) and mouse_y in range(5,25):
        mouse_over = True
    #gameover sel
    elif mouse_x in range(380,520) and mouse_y in range(305,335):
        mouse_over = True
    #stats sele
    elif mouse_x in range(325,570) and mouse_y in range(400,440):
        mouse_over = True
    elif mouse_x in range(320,580) and mouse_y in range(500,540):
        mouse_over = True
    else:
        mouse_over = False
    #---character movement settings---#
    if c_xspd == "right":
        c_x += 3
        delay += 1
    if c_xspd == "left":
        c_x -= 3
        delay += 1
    if c_xspd == "stop":
        c_x += 0
    if c_yspd == "stop":
        c_y += 0
    if c_yspd == "jump":
        c_y -= up
        j_time += 1
    if c_yspd == "grav":
        c_y += up
        d_time += 1
    #---#

    #---START---#
    if menu:                     
        #---DRAWING/TEXT---#
        screen.blit(background,(0,0))
        screen.blit(gname, (100,height*0.15))
                
        Menu = ("Story Mode",
                "Free Play",
                 "Controls",
                   "Quit")
        if pygame.font:
            menuHeight = (20+0)*len(Menu)
            startY = background.get_height()*0.3

            listOfTextPositions=list()

            for menuEntry in Menu:
                text = fontdata.font.render(menuEntry,1,(250, 250, 250))
                textpos = text.get_rect(centerx=background.get_width()/2,centery=startY+20+0 )
   
                listOfTextPositions.append(textpos)

                startY=startY+20+0
                
                screen.blit(text, textpos)
        if mouse_over:
            if mouse_x in range(390,500) and mouse_y in range(190,210):
                block = pygame.Surface((120,20), pygame.SRCALPHA)
                block.fill((255,255,255,128))
                screen.blit(block,(390,190))                
            elif mouse_x in range(390,500) and mouse_y in range(210,225):
                block = pygame.Surface((120,20), pygame.SRCALPHA)
                block.fill((255,255,255,128))
                screen.blit(block,(390,210))
            elif mouse_x in range(390,500) and mouse_y in range(230,245):
                block = pygame.Surface((120,20), pygame.SRCALPHA)
                block.fill((255,255,255,128))
                screen.blit(block,(390,230))
            elif mouse_x in range(390,500) and mouse_y in range(250,265):
                block = pygame.Surface((120,20), pygame.SRCALPHA)
                block.fill((255,255,255,128))
                screen.blit(block,(390,250))

    #---Controls Page---#
    if controlpageon:
        screen.blit(controlpage,(0,0))
        spritestor.controlpage.update()
        spritestor.controlpage.draw(screen)
        screen.blit(fontdata.font.render("Back to Menu",1,colordata.black),(35,7))
        screen.blit(backarrow,(5,5))

        if mouse_over:
            if mouse_x in range(5,180) and mouse_y in range(5,25):
                block = pygame.Surface((178,24), pygame.SRCALPHA)
                block.fill((255,255,255,128))
                screen.blit(block,(4,4))    
    #---level tutorial---#
    if ltut:
        #---DRAWING/TEXT---#
        if redraw_lv:
            maptutorial.create_level(spritestor.block_list,spritestor.all_sprites_list,spritestor.platforms)
            redraw_lv = False
                   
        screen.fill(colordata.beige)
        
        screen.blit(fontdata.scr.render(str(score),1,colordata.black),(415,10))
        screen.blit(fontdata.bit.render("HAT PWR LVL :"+" "+str(hatpl)+"%",1,colordata.black),(560,10))

        screen.blit(door1,(700,250))
        
        eventstart_basic()

        if introopen:
            screen.blit(intro,(0,0))
        if introopen1:
            screen.blit(intro1,(0,0))

        if event.type == pygame.KEYDOWN and event.key == pygame.K_e and introopen:
            introopen = False
            introopen1 = True
            pygame.time.wait(500)
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            introopen1 = False
        
        if pausing:
            pause()    
                            
    #---Story Mode---#
    if ls1:
        if clearlist:
            reset()

        screen.fill(colordata.beige)                   

        screen.blit(fontdata.scr.render(str(score),1,colordata.black),(415,10))
        screen.blit(fontdata.bit.render("HAT PWR LVL :"+" "+str(hatpl)+"%",1,colordata.black),(560,10))              

        newdoor()
        eventstart()
        newlevel()
        if pausing:
            pause()

    if ls2:
        if clearlist:
            reset()

        screen.fill(colordata.beige)                   

        screen.blit(fontdata.scr.render(str(score),1,colordata.black),(415,10))
        screen.blit(fontdata.bit.render("HAT PWR LVL :"+" "+str(hatpl)+"%",1,colordata.black),(560,10))              

        newdoor()
        eventstart()
        newlevel()
        if pausing:
            pause()
            
    if ls3:
        if clearlist:
            reset()

        screen.fill(colordata.beige)                   

        screen.blit(fontdata.scr.render(str(score),1,colordata.black),(415,10))
        screen.blit(fontdata.bit.render("HAT PWR LVL :"+" "+str(hatpl)+"%",1,colordata.black),(560,10))              

        newdoor()
        eventstart()
        newlevel()
        if pausing:
            pause()
            
    if ls4:
        if clearlist:
            reset()

        screen.fill(colordata.beige)                   

        screen.blit(fontdata.scr.render(str(score),1,colordata.black),(415,10))
        screen.blit(fontdata.bit.render("HAT PWR LVL :"+" "+str(hatpl)+"%",1,colordata.black),(560,10))              

        newdoor()
        eventstart()
        newlevel()
        if pausing:
            pause()

    if ls5:
        if clearlist:
            reset()

        screen.fill(colordata.beige)                   

        screen.blit(fontdata.scr.render(str(score),1,colordata.black),(415,10))

        eventstart()
        spritestor.bosstype.update()
        spritestor.bosstype.draw(screen)
        
        if pausing:
            pause()
    #---FREE PLAY---#
    if freeplay:
        if redraw_lv:
            sll = 2
            ssl = 4
            randsmalldelay = random.randrange(50,120)
            randlargedelay = random.randrange(120,180)
            mapl1.create_level(spritestor.block_list,spritestor.all_sprites_list,spritestor.platforms)
            redraw_lv = False
            
        screen.fill(colordata.beige)                   
        screen.blit(fontdata.scr.render(str(score),1,colordata.black),(415,10))
        eventstart()
        if pausing:
            pause()
    #---GAMEOVER SCREEN---#
    if gameoverpage:
        screen.fill(colordata.black)
        screen.blit(fontdata.fonts81.render("GAME OVER",1,colordata.white),(225,150))
        screen.blit(fontdata.fonts45.render("NEXT>",1,colordata.white),(390,300))

        if mouse_over:
            if mouse_x in range(380,520) and mouse_y in range(305,335):
                block = pygame.Surface((140,40), pygame.SRCALPHA)
                block.fill((255,255,255,128))
                screen.blit(block,(380,300))
    #STATS SCREEN
    if statistics:
        screen.fill(colordata.black)
        screen.blit(fontdata.fonts81.render("STATISTICS",1,colordata.white),(225,25))
        screen.blit(fontdata.fonts45.render("CONTINUE?",1,colordata.white),(335,400))
        screen.blit(fontdata.fonts45.render("MAIN MENU",1,colordata.white),(325,500))
        screen.blit(fontdata.fonts36.render("YOUR SCORE: "+str(score),1,colordata.white),(100,150))
        screen.blit(fontdata.fonts36.render("NUMBER OF ATTACKS: "+str(attacknum),1,colordata.white),(100,200))
        screen.blit(fontdata.fonts36.render("DINOGATORS REMOVED FROM WORLD: "+str(kills),1,colordata.white),(100,250))
        screen.blit(fontdata.fonts36.render("CONTINUES USED: "+str(contuse),1,colordata.white),(100,300))

        if mouse_over:
            if mouse_x in range(325,570) and mouse_y in range(400,440):
                block = pygame.Surface((250,40), pygame.SRCALPHA)
                block.fill((255,255,255,128))
                screen.blit(block,(325,400))
            if mouse_x in range(320,580) and mouse_y in range(500,540):
                block = pygame.Surface((255,40), pygame.SRCALPHA)
                block.fill((255,255,255,128))
                screen.blit(block,(320,500))
    #---GAMEFINISH---#
    if gamefinish:
        bossfite.fadeout(5)
        screen.fill(colordata.black)
        screen.blit(fontdata.fonts45.render("YOU DEFEATED THE HATNABBER!",1,colordata.white),(75,150))
        screen.blit(fontdata.fonts45.render("NEXT>",1,colordata.white),(390,300))

        if mouse_over:
            if mouse_x in range(380,520) and mouse_y in range(305,335):
                block = pygame.Surface((140,40), pygame.SRCALPHA)
                block.fill((255,255,255,128))
                screen.blit(block,(380,300))
    if gfstatistics:
        screen.fill(colordata.black)
        screen.blit(fontdata.fonts81.render("STATISTICS",1,colordata.white),(225,25))
        screen.blit(fontdata.fonts45.render("CONTINUE>",1,colordata.white),(335,400))
        screen.blit(fontdata.fonts36.render("YOUR SCORE: "+str(score),1,colordata.white),(100,150))
        screen.blit(fontdata.fonts36.render("NUMBER OF ATTACKS: "+str(attacknum),1,colordata.white),(100,200))
        screen.blit(fontdata.fonts36.render("DINOGATORS REMOVED FROM WORLD: "+str(kills),1,colordata.white),(100,250))
        screen.blit(fontdata.fonts36.render("CONTINUES USED: "+str(contuse),1,colordata.white),(100,300))
        if mouse_over:
            if mouse_x in range(325,570) and mouse_y in range(400,440):
                block = pygame.Surface((250,40), pygame.SRCALPHA)
                block.fill((255,255,255,128))
                screen.blit(block,(325,400))

    if ending:
        screen.blit(end,(0,0))

        if event.type == pygame.KEYDOWN and event.key == pygame.K_e:
            title.play(-1)
            reset()
            ending = False
            menu = True
            ltut = False
            ls1 = False
            ls2 = False
            ls3 = False
            ls4 = False
            ls5 = False
            redraw_lv = True
            freeplay = False
            gameoverpage = False
            done = False
            movement = False
            mouse_over = False
            statistics = False
            clearlist = False
            spawning = True
            spawningsmall = True
            spawninglarge = True
            spawnedsmall = 0
            spawnedlarge = 0
            spawndelay = 0
            randsmalldelay = 0
            randlargedelay = 0
            ssl = 2
            sll = 0
            contuse = 0
            mlnormal = True
            mlaggrav = False
            mlfspd = 8
            mlhealth = 10
            mltimebetween = 7
            mldelay = 0
            normal = True
            aggrav = False
            mob_health = 5
            mfspd = 7
            timebetween = 7
            mdelay = 0
            stopped = False
            stoptime = 0
            attackchoice = 0
            tooclose = False
            xdist = 90
            followx = True
            followy = True
            bossfaceleft = False
            c_yspd = "stop"
            c_xspd = "stop"
            javail = True
            rightavail = True
            attackavail = True
            leftavail = True
            invuln = False
            invulntimer = 0
            holding_weapon = False
            j_time = 0
            d_time = 0
            master = True
            pwrgain = 10
            attacknum = 0
            kills = 0
            hatpl = 0
            delay = 0
            indicate = False
            indicatedelay = 0
            setpos = True
            randwep = 0
            javelin_wep = False
            catcannon_wep = False
            leafblower_wep = False
            watergun_wep = False
            rainbowgun_wep = False
            gamefinish = False
            gfstatistics = False
            c_x = 100
            c_y = 300
            score = 0
            spritestor.block_list.empty()
            spritestor.all_sprites_list.empty()
            spritestor.platforms.empty()
            spritestor.smallenemies.empty()
            spritestor.largeenemies.empty()
            spritestor.flyingenemies.empty()
            spritestor.onhand.empty()
            spritestor.all_sprites_list.add(player)
    #---Debug---#
    if debug:
        debug_on = True
        p_health = 10
        screen.blit(fontdata.dfont.render("Player y motion: "+str(c_yspd),1,(255,20,147)),(5,0))
        screen.blit(fontdata.dfont.render("Player x motion: "+str(c_xspd),1,(255,20,147)),(5,20))
        screen.blit(fontdata.dfont.render("Player pos (x,y): "+str(c_x)+" "+str(c_y),1,(255,20,147)),(5,40))
        screen.blit(fontdata.dfont.render("Descend time: "+str(d_time),1,(255,20,147)),(5,60))
        screen.blit(fontdata.dfont.render("Jump time: "+str(j_time),1,(255,20,147)),(5,80))
        screen.blit(fontdata.dfont.render("Data: "+str(attackchoice)+str(newlev),1,(255,20,147)),(5,100))
        screen.blit(fontdata.dfont.render("Framerate: "+str(int(clock.get_fps())),1,(255,20,147)),(750,0))
       
    #---SCREEN FPS---#
    pygame.display.flip()
    clock.tick(60)
#---END LOOP---#
pygame.quit()
 
