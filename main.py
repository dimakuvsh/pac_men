import pygame as pg
import random

class Bird1(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("images/bird1.png")
        self.image = pg.transform.scale(self.image, (80, 80))

        self.rect = self.image.get_rect()

        self.rect.center = (40, 40)
        
        self.direction = "right"
    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_a] and self.rect.left > 0:
            if self.direction == "right":
                self.image = pg.transform.flip(self.image, True, False)
                self.direction = "left"
            self.rect.x -= VELOCITY

        if keys[pg.K_d] and self.rect.right < WINDOW_WIDTH:
            if self.direction == "left":
                self.image = pg.transform.flip(self.image, True, False)
                self.direction = "right"
            self.rect.x += VELOCITY

        if keys[pg.K_w] and self.rect.top > 0:
                self.rect.y -= VELOCITY
        if keys[pg.K_s] and self.rect.bottom < WINDOW_HIGHT:
            self.rect.y += VELOCITY 
class Bird2(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("images/bird2.png")
        self.image = pg.transform.scale(self.image, (80, 80))

        self.rect = self.image.get_rect()

        self.rect.center = (40, 150)
        
        self.direction = "right"
    def update(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and self.rect.left > 0:
            if self.direction == "right":
                self.image = pg.transform.flip(self.image, True, False)
                self.direction = "left"
            self.rect.x -= VELOCITY

        if keys[pg.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            if self.direction == "left":
                self.image = pg.transform.flip(self.image, True, False)
                self.direction = "right"
            self.rect.x += VELOCITY

        if keys[pg.K_UP] and self.rect.top > 0:
                self.rect.y -= VELOCITY
        if keys[pg.K_DOWN] and self.rect.bottom < WINDOW_HIGHT:
            self.rect.y += VELOCITY      
class Pig(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load("images/pig.png")
        self.image = pg.transform.scale(self.image, (80, 80))

        self.rect = self.image.get_rect()
        self.rect.center = (WINDOW_WIDTH//2,WINDOW_HIGHT//2)
pg.init()

WINDOW_WIDTH = 800
WINDOW_HIGHT = 600
size = (WINDOW_WIDTH, WINDOW_HIGHT)
screen = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HIGHT))
pg.display.set_caption("Angri bird")

bird1 = Bird1()
bird2 = Bird2()
pig = Pig()
FPS = 120
clock = pg.time.Clock()

background = pg.image.load("images/background.webp")
background = pg.transform.scale(background, size)

BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
#скорость движения птицы
VELOCITY = 3
#количество очков
score1 = 0
score2 = 0
running = True
font = pg.font.Font("fonts/Pacifico-Regular.ttf",40)
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    pig.update()
    bird1.update()
    bird2.update()
    if bird1.rect.colliderect(pig.rect) == True:
        x = random.randint(0, WINDOW_WIDTH - pig.rect.w)
        y = random.randint(0, WINDOW_HIGHT - pig.rect.h)
        pig.rect.left = x
        pig.rect.top = y
        score1 += 1
    if bird2.rect.colliderect(pig.rect) == True:
        x = random.randint(0, WINDOW_WIDTH - pig.rect.w)
        y = random.randint(0, WINDOW_HIGHT - pig.rect.h)
        pig.rect.left = x
        pig.rect.top = y
        score2 += 1
    

    #отрисовка спрайта 
    screen.blit(background, (0, 0))
    screen.blit(bird1.image, bird1.rect)
    screen.blit(bird2.image, bird2.rect)
    screen.blit(pig.image, pig.rect)
    #отрисовка счёта
    score_text1 = font.render(str(score1), True, "gold")
    score_text2 = font.render(str(score2), True, "black")
    screen.blit(score_text1, (20,10))
    screen.blit(score_text2, (WINDOW_WIDTH - 50,10))
    
    
    
    pg.display.update()

    clock.tick(FPS)



pg.quit()