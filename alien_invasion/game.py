import sys
import pygame

from alien import Alien
from bullet import Bullet
from ship import Ship

class Game:
    def __init__(self, title):
        pygame.init()
        self.title = title
        self.screen_surf = pygame.display.set_mode(size=(800, 640))
        pygame.display.set_caption(self.title)

        self.ship = Ship(self.screen_surf)
        self.ship.move_midbottom()

        self.aliens = []
        for i in range(8):
            for j in range(10):
                alien = Alien(self.screen_surf)
                x_pos = 80 + (80 * 2) * j
                y_pos = 50 + 50 * (50 * 2) * i
                alien.move(x_pos, y_pos)
                self.aliens.append(alien)

        self.bullets = []

        self.clock = pygame.time.Clock()

    def start(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.ship.move_left(5)
                    elif event.key == pygame.K_RIGHT:
                        self.ship.move_right(5)
                    elif event.key == pygame.K_SPACE:
                        self.fire_bullet()

            self.screen_surf.fill((255, 255, 255))
            self.ship.render()
            for alien in self.aliens:
                alien.render()
            for bullet in self.bullets:
                bullet.move()
                bullet.render()

            pygame.display.flip()
            self.clock.tick(60)

    def fire_bullet(self):
        bullet = Bullet(self.screen_surf, self.ship.ship_rect)
        self.bullets.append(bullet)