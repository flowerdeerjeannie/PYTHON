import pygame
#초기화
pygame.init()
#화면 설정
screen_surf = pygame.display.set_mode((1280,720))
ship_img = pygame.image.load('./images/ship.bmp')
alien_img = pygame.image.load('./images/alien.bmp')

#rect-위치, 기본으로는 사각형형태
ship_rect = ship_img.get_rect()
ship_rect.midbottom = screen_surf.get_rect().midbottom

alien_rect = alien_img.get_rect()
# 외계인들을 위한 리스트
aliens = []
for i in range(20):
    # 각각의 외계인 객체를 생성하여 리스트에 추가
    alien = pygame.rect.Rect(100 + 100*i, 100, 100, 100)
    aliens.append(alien)


#총알 위치 초기화 후 배열 생성, 그리고 우주선 정중앙 상단에 위치하게 위치설정
bullet_rect = None
bullets = []

clock = pygame.time.Clock()

# 누르고 있을 때도 실행되도록
left_pressed = False
right_pressed = False
up_pressed = False
down_pressed = False
# alien이 자동으로 움직이도록
aliens_x_direction = 1 # 1은 오른쪽, -1은 왼쪽
aliens_y_direction = 1
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
                    #게임 화면에 총알이 표시되는 위치가X, 총알객체가 생성될때의 초기 위치를 설정
                    bullet_rect=pygame.rect.Rect(0,0,500,10)
                    #이건 실제로 표시되는 위치
                    bullet_rect.midbottom=ship_rect.midtop
                    bullets.append(bullet_rect)
                elif event.key == pygame.K_q:
                    pygame.quit()
                    raise SystemExit
            elif event.key == pygame.K_RIGHT:
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

    # Do logical updates here.
    
    if is_running:          
        if right_pressed:
            #스크린 surface의 위치와 크기를 get해서 screen_rect에 저장함
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

        if bullets:
            screen_rect = screen_surf.get_rect()
            for bullet in bullets:
                if bullet.y <0:
                    bullets.remove(bullet)
                    #게임에서 화면 밖으로 나가거나 더 이상 화면에 표시할 필요가 없는 요소를 정리
            for bullet_rect in bullets:
                bullet_rect.y -= 10 


    # 총알들의 움직임 업데이트
    # 총알들이 위로 이동

    screen_rect = screen_surf.get_rect()


    for alien in aliens:
        alien.x += 2 * aliens_x_direction
        if alien.right >= screen_rect.width + 50 or alien.left <= 0:
            aliens_x_direction *= -1
            alien.y += 10

    screen_surf.fill((0,0,0))
     # Fill the display with a solid color

    # Render the graphics here.
    # ...
    # 우주선과 외계인들을 그림
    screen_surf.blit(ship_img, ship_rect)
    for alien in aliens:
          screen_surf.blit(alien_img, alien)

    # 총알을 그림
    for bullet in bullets:
        
        pygame.draw.rect(screen_surf, 'red', bullet)

   # 총알과 외계인들의 충돌 감지
    for alien in aliens:
        for bullet in bullets[:]:  # bullets 리스트를 직접 수정하므로 [:]를 사용하여 복사본을 반복
             if alien.colliderect(bullet):
                 bullets.remove(bullet)
                 aliens.remove(alien)
                 break  # 내부 루프를 빠져나옴
    pygame.display.flip()  # Refresh on-screen display
    clock.tick(60)         # wait until next frame (at 60 FPS)