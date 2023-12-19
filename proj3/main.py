import pygame
from time import time
from player import player
from bullet import bullet
from ImageManager import ImageManager

#import block

WIDTH = 128
HEIGHT = 96

#init asset manager
manager = ImageManager()
manager.load_all_sprites()

# Initialize Pygame
pygame.init()
    
# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Create the game window

screen = pygame.display.set_mode((WIDTH, HEIGHT),pygame.FULLSCREEN)
#screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Define In-game variables
dir_p1 = "assets//p1.png"
dir_p2 = "assets//p2.png"
p1 = player('cat')
p1.x = 0
p1.y = 16
p1.side = 0

p2 = player('hamster')
p2.x = 112
p2.y = 80
p2.side = 1

bullet_arr = []

inputs = []
FPS = 30
current = time()
elapsed = time()
running = True
last_event = []
current_event = []
new_bullet = bullet((0,0),0, 0)

while running:
    for event in pygame.event.get():#get input
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        running = False

    
    if (elapsed - current > 1/FPS):#update sprites
        for event in last_event:#handle major events
            #print("checking events")
            if event["type"] == "spawn":
                if event["target"] == "bullet":
                    #print("bullet is spawning")
                    tmp = new_bullet
                    tmp.x = event["pos"][0]
                    tmp.y = event["pos"][1]
                    tmp.direction = event["vector"]
                    tmp.side = event["side"]
                    
                    #tmp = bullet(event["pos"],event["vector"],event["side"])
                    bullet_arr.append(tmp)
                    del tmp
                    #print("bullet is spawned")
                elif event["target"] == "item":
                    pass

        #delete dead bullets
        for i in range(len(bullet_arr)):
            if bullet_arr[i].dead == True:
                trash = bullet_arr[i]
        
        #real update sprites
        current_event.append(p1.update(keys,last_event, manager))
        for i in range(len(bullet_arr)):
            bullet_arr[i].update()
            #print("bullet is updated")
        
        #update frame variables
        current = time()
        last_event = current_event
        current_event = []
        
    #render all sprites
    screen.fill(BLACK)
    

    for bullet in bullet_arr:
        bullet.render(manager, screen)
        #print("bullet is rendered")
    p1.render(manager, screen)
    p2.render(manager, screen)
    
    pygame.display.flip()

    #reset frame variables
    inputs = []
    elapsed = time()
        
pygame.quit()
