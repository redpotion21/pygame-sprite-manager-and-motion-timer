from sprite import sprite

class bullet(sprite):

    def __init__(self, pos, direction, side):
        self.speed = 2
        self.life = 60
        self.dead = False
        self.side = side
        self.direction = direction
        self.x = pos[0]
        self.y = pos[1]
        self._sprite__set_img_id('bullet')
        self.set_motion_state('idle')

    def update(self):
        if self.life == 0:
            self.dead = True
        
        if self.direction==0:
            self.x -= self.speed
        elif self.direction==1:
            self.y+=self.speed
        elif self.direction==2:
            self.x+=self.speed
        elif self.direction==3:
            self.y-=self.speed
        
        
        #update frame parameters
        self.life -=1
