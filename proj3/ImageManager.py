import pygame
import os

print("image manager opened")

class ImageManager():
    sprites = {}#FORMAT NAME_STATE_NUMBER
    tiles = {}
    default_image = [[[255,255,255] for i in range(16)] for j in range(16)]

    def load(self, directory, img_type, name, tag, idx = 0):
        tmp = pygame.image.load(directory)
        if img_type == 'sprites' or img_type == 's':
            sprite[name + '_' + tag + '_' + str(idx)] = tmp
        elif img_type == 'tiles' or img_type == 't':
            tiles[name + '_' + tag + '_' + str(idx)] = tmp
        else:
            print("invalid image type")
            
    def get(self,img_type, name, tag, idx):
        try:
            
            if img_type == 'sprites' or img_type == 's':
                return ImageManager.sprites[name + '_' + tag + '_' + str(idx)]
            elif img_type == 'tiles' or img_type == 't':
                return ImageManager.tiles[name + '_' + tag + '_' + str(idx)]
            else:
                print("invalid image type")
        except KeyboardInterrupt:
            print('index error')
            return ImageManager.default_image

    def load_all_sprites(self):#loads all sprite in /sprite (MUST SATISFY THE FORMAT)
        path = "assets//sprites"
        files = os.listdir(path)

        for file in files:
            tmp = pygame.image.load(path + '//' + file)
            self.sprites[file[0:len(file)-4]] = tmp

        print("image load all completed")   













        
        
    
