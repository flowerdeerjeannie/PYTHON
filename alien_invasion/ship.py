import pygame


class Ship:
     def __init__(self, screen_surf):
          self.ship_img_surf = pygame.image.load('images/ship.bmp').convert()
          self.ship_rect = self.ship_img_surf.get_rect()
          self.screen_surf = screen_surf
     
     def render(self):
          self.screen_surf.blit(self.ship_img_surf, self.ship_rect)

     def move_midbottom(self):
          self.ship_rect.midbottom = self.screen_surf.get_rect().midbottom

     def move_left(self, distance):
        self.ship_rect.x -= distance
        self.check_boundary()

     def move_right(self, distance):
        self.ship_rect.x += distance
        self.check_boundary()

     def check_boundary(self):
        screen_rect = self.screen_surf.get_rect()
        if self.ship_rect.right > screen_rect.right:
            self.ship_rect.right = screen_rect.right
        elif self.ship_rect.left < 0:
            self.ship_rect.left = 0

