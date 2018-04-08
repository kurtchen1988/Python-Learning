import pygame
from pygame.locals import *
import time, random

class HeroPlane:
    def __init__(self, screen_temp):
        self.x = 200
        self.y = 400
        self.screen_temp = screen_temp
        self.image = pygame.image.load("./images/me.png")
        self.bullet_list = []

    def display(self):

        for b in self.bullet_list:
            b.display()
            if b.move():
                self.bullet_list.remove(b)
        self.screen_temp.blit(self.image, (self.x, self.y))

    def move_left(self):
        self.x -= 5
        if self.x<=0:
            self.x=0

    def move_right(self):
        self.x += 5
        if self.x>=406:
            self.x=406

    def fire(self):
        self.bullet_list.append(bullet(self.screen_temp, self.x, self.y))
        print()

class bullet:
    def __init__(self, screen_temp, x, y):
        self.x = x +53
        self.y = y
        self.screen_temp = screen_temp
        self.image = pygame.image.load("./images/pd.png")

    def display(self):
        self.screen_temp.blit(self.image,(self.x,self.y))


    def move(self):
        self.y-=10
        if self.y <= -20:
            return True

class EnemyPlane:
    def __init__(self, screen_temp):
        self.x = random.choice(range(408))
        self.y = -75
        self.screen_temp = screen_temp
        self.image = pygame.image.load("./images/e"+str(random.choice(range(3)))+".png")

    def display(self):
        self.screen_temp.blit(self.image,(self.x,self.y))


    def move(self, hero):
        self.y += 4

        if self.y>468:
            return True

        for bo in hero.bullet_list:
            if(bo.x>self.x+12 and bo.x<self.x+92 and bo.y+20 and bo.y<self.y+60):
                hero.bullet_list.remove(bo)
                return True




def key_control(hero_temp):

    for event in pygame.event.get():
        if event.type == QUIT:
            print("exit()")
            exit()

    pressed_keys = pygame.key.get_pressed()
    #print(pressed_keys)
    if pressed_keys[K_LEFT] or pressed_keys[K_a]:
        print("Left...")
        hero_temp.move_left()
    elif pressed_keys[K_RIGHT] or pressed_keys[K_d]:
        print("Right...")
        hero_temp.move_right()
    if pressed_keys[K_SPACE]:
        print("space...")
        hero_temp.fire()

def main():

    screen = pygame.display.set_mode((512,568),0,0)

    background = pygame.image.load("./images/bg2.jpg")
    hero = HeroPlane(screen)

    m = -968
    enemylist = []

    while True:

        screen.blit(background,(0,m))
        m+=2
        if m>=-200:
            m = -968
        hero.display()
        key_control(hero)

        if random.choice(range(50))==10:
            enemylist.append(EnemyPlane(screen))
        for em in enemylist:
            em.display()
            if em.move(hero):
                enemylist.remove(em)

        pygame.display.update()

        time.sleep(0.04)

if __name__ == '__main__':

    main()