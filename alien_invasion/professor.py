
import pygame

pygame.init()

screen_surf = pygame.display.set_mode((1280,720))
game_over_msg = pygame.font.Font(None, 64)
# screen_surf = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

ship_img = pygame.image.load('images/ship.bmp')
alien_img = pygame.image.load('images/alien.bmp')

ship_rect = ship_img.get_rect()
ship_rect.midbottom = screen_surf.get_rect().midbottom

alien_rect = alien_img.get_rect()
alien_x_pos = alien_rect.width
alien_y_pos = alien_rect.height

aliens = []
for _ in range(10):
    alien = pygame.rect.Rect(alien_x_pos, alien_y_pos,\
                            alien_rect.width,\
                            alien_rect.height)
    alien_x_pos += alien_rect.width * 2
    aliens.append(alien)

bullet_rect = None
bullets = []

clock = pygame.time.Clock()

left_pressed = False
right_pressed = False
alien_x_direction = 1 # False: -1, 1: right
alien_x_direction_changed = False
is_running = True

while True:

    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if len(bullets) < 5:
                    bullet_rect = pygame.rect.Rect(0, 0, 500, 10)
                    bullet_rect.midbottom = ship_rect.midtop
                    bullets.append(bullet_rect)
            elif event.key == pygame.K_q:
                pygame.quit()
                raise SystemExit
            elif event.key == pygame.K_RIGHT:
                right_pressed = True
            elif event.key == pygame.K_LEFT:
                left_pressed = True
            elif event.key == pygame.K_UP:
                ship_rect.y = ship_rect.y - 10
                alien_rect.y = alien_rect.y - 20
            elif event.key == pygame.K_DOWN:
                ship_rect.y = ship_rect.y + 10
                alien_rect.y = alien_rect.y + 20
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                right_pressed = False    
            elif event.key == pygame.K_LEFT:
                left_pressed = False

    if is_running:          
        if right_pressed:
            screen_rect = screen_surf.get_rect()
            if ship_rect.x < screen_rect.width - ship_rect.width:
                ship_rect.x = ship_rect.x + 10
            if alien_rect.x < screen_rect.width - alien_rect.width:
                alien_rect.x = alien_rect.x + 20
       
        if left_pressed:
            if 0< ship_rect.x:
                ship_rect.x = ship_rect.x - 10
            if 0< alien_rect.x:
                alien_rect.x = alien_rect.x - 20

        if aliens:
            screen_rect = screen_surf.get_rect()
            for alien in aliens:
                if screen_rect.width - alien.width < alien.x:
                    alien_x_direction = -1
                    alien_x_direction_changed = True
                    break
                elif alien.x < screen_rect.x:
                    alien_x_direction = 1
                    alien_x_direction_changed = True
                    break

            for alien in aliens:
                print(alien.y, alien_y_pos)
                alien.x += alien_x_direction * 2
                if alien_x_direction_changed:
                    alien.y += alien_img.get_rect().height

        alien_x_direction_changed = False
       
        if bullets:
            screen_rect = screen_surf.get_rect()
           
            for bullet in bullets:
                if bullet.y < 0:
                    bullets.remove(bullet)
           
            for bullet in bullets:
                bullet.y = bullet.y - 10
       
        for alien in aliens:
            for bullet in bullets:
                if pygame.rect.Rect.colliderect(alien, bullet):
                    aliens.remove(alien)
                    bullets.remove(bullet)
       
        if len(aliens) == 0:
            print('Game Over!')
            is_running = False
       

    screen_surf.fill('white')  # Fill the display with a solid color
    game_over_msg.render('Game Over!', True, (0, 0, 0))

    # Render the graphics here.
    screen_surf.blit(ship_img, ship_rect)
    #screen_surf.blit(alien_img, alien_rect)
    if aliens:
        for alien in aliens:
            screen_surf.blit(alien_img, alien)
    if bullets:
        for bullet in bullets:
            pygame.draw.rect(screen_surf, 'red', bullet)
    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)
