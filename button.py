import pygame

class Button():
    def __init__(self, screen, msg, left,top):  # msg noi dung cua button
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.width, self.height = 150, 50  
        self.button_color =  (46, 139, 87)
        self.text_color = (255, 255, 255)  
        pygame.font.init()
        self.font = pygame.font.SysFont('kaiti', 50)  

        self.rect = pygame.Rect(left, top, self.width, self.height)
        #self.rect.center = self.screen_rect.center  
        self.left = left
        self.top = top

        self.deal_msg(msg)  

    def deal_msg(self, msg):
        self.msg_img = self.font.render(msg, True, self.text_color, self.button_color)  
        self.msg_img_rect = self.msg_img.get_rect()  
        self.msg_img_rect.center = self.rect.center  
        self.msg_img_rect.width = self.width
        self.msg_img_rect.height = self.height
        

    def draw_button(self): 
        self.screen.blit(self.msg_img, (self.left,self.top)) 
        #self.screen.blit(self.msg_img, self.msg_img_rect) 

    def is_click(self):
        point_x, point_y = pygame.mouse.get_pos()
        x = self.left
        y = self.top
        w, h = self.msg_img.get_size()

        in_x = x < point_x < x + w
        in_y = y < point_y < y + h
        
        if in_x and in_y and pygame.mouse.get_pressed()[0] == 1:
            return True
        else:
            return False

