import pygame

pygame.init()

screen_surf = pygame.display.set_mode((1280,720))

ship_img = pygame.image.load('./images/ship.bmp')
alien_img = pygame.image.load('./images/alien.bmp')

#rect-위치, 기본으로는 사각형형태
ship_rect = ship_img.get_rect()
ship_rect.midbottom = screen_surf.get_rect().midbottom
#x.y.그 점에서의 사각형을 만들어 width.height
alien_rect=pygame.rect.Rect(200,200,200,200)

bullet_rect = None
bullets = []

bullet_rect=pygame.rect.Rect(0, 0, 5, 20)
bullet_rect.midbottom=ship_rect.midtop

clock = pygame.time.Clock()

left_pressed = False
right_pressed = False
up_pressed = False
down_pressed = False

while True:
    # Process player inputs.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            raise SystemExit
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet_rect.midbottom=ship_rect.midtop
                bullets.append(bullet_rect)
            if event.key == pygame.K_RIGHT:
                right_pressed= True
            elif event.key == pygame.K_LEFT:
                left_pressed= True
            elif event.key == pygame.K_UP:
                up_pressed = True        
            elif event.key == pygame.K_DOWN:
                down_pressed = True                     
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                right_pressed = False
            elif event.key == pygame.K_LEFT:
                left_pressed = False
            elif event.key == pygame.K_UP:
                up_pressed = False
            elif event.key == pygame.K_DOWN:
                down_pressed = False

    # Do logical updates here.
    if right_pressed:
        ship_rect.x = ship_rect.x + 10
        alien_rect.x = alien_rect.x + 20
    elif left_pressed:
        ship_rect.x = ship_rect.x - 10
        alien_rect.x = alien_rect.x - 20
    elif up_pressed:
        ship_rect.y = ship_rect.y - 5
        alien_rect.y = alien_rect.y - 10    
    elif down_pressed:
        ship_rect.y = ship_rect.y + 5
        alien_rect.y = alien_rect.y + 10 
    if bullets:
        for bullet in bullets:
            bullet_rect.y = bullet_rect.y - 3


    screen_surf.fill('white')  # Fill the display with a solid color

    # Render the graphics here.
    # ...
    screen_surf.blit(ship_img, ship_rect)
    screen_surf.blit(alien_img, alien_rect)
    if bullets:
        for bullet in bullets:
            pygame.draw.rect(screen_surf, 'red', bullet_rect)
    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)