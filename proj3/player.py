from sprite import sprite
import pygame


class player(sprite):
    
    def __init__(self, Name):
        super().__init__()
        self.hp = 10
        self.speed = 1
        self.atk = 1
        self.atk_delay = 30
        self.direction = 0
        self.action_string = ['left', 'down', 'right', 'up']
        self.is_attacking = 0
        self.side = 0
        self._sprite__set_img_id(Name)
        

    def update(self, keys, event, ImageManager):

        new_state = 'default'
        going = False
        events = {}
        
        if keys[pygame.K_LEFT]:
            going = True
            if self.x -self.speed <0:
                self.x = 0
            else:
                self.x-=self.speed
            self.direction = 0
        
        elif keys[pygame.K_RIGHT]:
            going = True
            if self.x +self.speed >112:
                self.x = 112
            else:
                self.x+=self.speed
            self.direction = 2
            
        elif keys[pygame.K_UP]:
            going = True
            if self.y -self.speed <16:
                self.y = 16
            else:
                self.y-=self.speed
            self.direction = 3
        
        elif keys[pygame.K_DOWN]:
            going = True
            if self.y +self.speed >80:
                self.y = 80
            else:
                self.y+=self.speed
            self.direction = 1

        
        if keys[pygame.K_SPACE] and self.atk_delay==0:
            self.atk_delay = 30
            self.is_attacking = 1
            events = {"type":"spawn", "target":"bullet", "pos":(self.x, self.y), "vector":self.direction, "side":self.side}
            #print("event sended")
            
        #update frame parameters
        if self.atk_delay>0:
            self.atk_delay-=1
        
        if self.atk_delay == 0:
            self.is_attacking = 0

        #update motion
        if self.is_attacking == 0:
            if going:
                self._sprite__update_motion(ImageManager, self.action_string[self.direction])
        else:
            self._sprite__update_motion(ImageManager, self.action_string[self.direction] + 'atk')
        
        #return all events
        if len(events) ==0:
            return {"type":"None"}
        else:
            return events
            
        
