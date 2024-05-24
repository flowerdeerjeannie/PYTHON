import pygame

class Bullet:
    def __init__(self, screen_surf, ship_rect):
        self.bullet_rect = pygame.Rect(0, 0, 10, 50)
        self.bullet_rect.midbottom = ship_rect.midtop
        self.screen_surf = screen_surf
        self.color = (255, 0, 0)  # 빨간색

    def move(self):
        self.bullet_rect.y -= 5

    def render(self):
        pygame.draw.rect(self.screen_surf, self.color, self.bullet_rect)


# bullet = Bullet()
# bullet.move_front_ship(ship_rect)
# bullet.render()