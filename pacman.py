import pygame
import neat
import os
import random

WIN_WIDTH = 720
WIN_HEIGHT = 480 


PACMAN_IMG = pygame.transform.scale(pygame.image.load("imgs/pacman-open.png"),(30,30)), pygame.transform.scale(pygame.image.load("imgs/pacman-closed.png"),(30,30))
GHOST_IMG = pygame.transform.scale(pygame.image.load("imgs/ghost.png"),(30,30))
BACKGROUND_IMG = pygame.transform.scale(pygame.image.load("imgs/background.jpg"),(1000,1000))
WALL_IMG = pygame.transform.scale(pygame.image.load("imgs/wall.png"),(30,30))

class pacman:
    IMGS = PACMAN_IMG
    

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.rotation = 0
        self.img_count = 0
        self.img = self.IMGS[0]
        self.tick_count = 0
        self.direction = "right"
        self.rotation = 0

    
    def move(self, direction):
        self.tick_count += 0.5
        if direction == "right":      
            self.x += 5
            self.rotation = 0
        elif direction == "left":
            self.x -= 5
            self.rotation = 180
        elif direction == "up":
            self.y -= 5
            self.rotation = 90
        elif direction == "down":
            self.y += 5
            self.rotation = 270

    def draw(self, win):
        self.img_count += 1

        # print(self.tick_count)
        if self.tick_count % 2 == True:
            self.img = self.IMGS[1]
        elif self.img_count % 2 == False:
            self.img = self.IMGS[0]
            self.img_count = 0

        rotated_pacman_image = pygame.transform.rotate(self.img, self.rotation)
        win.blit(rotated_pacman_image,(self.x,self.y))

    def get_mask(self):
        return pygame.mask.from_surface(self.img)

class ghost:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        return

class wall:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.img = WALL_IMG

    def draw(self,win):
        win.blit(self.img, (self.x, self.y))

    def get_mask(self):
        return pygame.mask.from_surface(self.img)

    def collide(self, pman_mask):
        pacman_mask = pman_mask
        wall_mask = self.get_mask()

        if pygame.sprite.collide_mask(pacman_mask, wall_mask) == True:
            print("Collision")



def game_map(win):
    map =  [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

    x = 0
    y = 0

    for i in map:     
        for k in i:           
            if k == 1:
                wall(x,y).draw(win)
            x += 30
        x = 0
        y += 30


def game_window(win, pman, direction):
    win.blit(BACKGROUND_IMG, (0,0))
    pman.move(direction)
    pman.draw(win)
    game_map(win)
    

    pygame.display.update()


def main():
    pygame.display.set_caption("Pacman")
    win = pygame.display.set_mode((WIN_WIDTH,WIN_HEIGHT))
    clock = pygame.time.Clock()
    direction = "right"
    pygame.display.flip()
    pman = pacman(30,30)
    walltest = wall(0,0)
    
    
    run = True
    while run:
        clock.tick(25)
        for event in pygame.event.get():
            pacman_mask = pman.get_mask()
            wall_mask = walltest.get_mask()

            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    direction = "right"
                if event.key == pygame.K_LEFT:
                    direction = "left"
                if event.key == pygame.K_DOWN:
                    direction = "down"
                if event.key == pygame.K_UP:
                    direction = "up"

            elif wall.collide(pacman_mask, 1) == True:
                return print("Ouch!")

        game_window(win, pman, direction)


        

if __name__ == "__main__":
    main()