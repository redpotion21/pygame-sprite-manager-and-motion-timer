import pygame

class sprite:
    delay_table = {'left_0': 5,
                   'left_1': 5,
                   'left_2': 5,
                   'left_3': 5,
                   'down_0': 5,
                   'down_1': 5,
                   'down_2': 5,
                   'down_3': 5,
                   'right_0': 5,
                   'right_1': 5,
                   'right_2': 5,
                   'right_3': 5,
                   'up_0': 5,
                   'up_1': 5,
                   'up_2': 5,
                   'up_3': 5,
                   'leftatk_0': 30,
                   'downatk_0': 30,
                   'rightatk_0': 30,
                   'upatk_0': 30,
                   'idle_0': 1}
    
    def __init__(self):
        self.x = 0
        self.y = 0
        self.name = None
        self.state = 'left'
        self.motion_index = 0
        self.motion_timer = 0
        

    def __set_img_id(self, Name):
        self.name = Name

    def set_motion_state(self, state_to):
        self.state = state_to
        self.motion_index = 0
        self.motion_timer = sprite.delay_table[self.state + '_' + str(self.motion_index)]
        
    def __update_motion(self, ImageManager, new_state):
        #print(new_state)
        if self.state != new_state:#change motion state if state is changed
            self.set_motion_state(new_state)
            self.motion_timer += 1
        
        if self.motion_timer !=0:#update timer
            self.motion_timer -=1
        else:# rotate to next index
            try:
                trash = ImageManager.get("sprites", self.name, self.state, self.motion_index + 1)
                self.motion_index += 1
                self.motion_timer = sprite.delay_table[self.state + '_' + str(self.motion_index)]
            except KeyError:#if there's no index forward, go to index 0
                self.motion_index = 0
                self.motion_timer = sprite.delay_table[self.state + '_' + str(self.motion_index)]
                
    def render(self, ImageManager, screen):
        tmp_img = ImageManager.get("sprites", self.name, self.state, self.motion_index)
        #print(tmp_img)
        screen.blit(tmp_img, (self.x, self.y))
