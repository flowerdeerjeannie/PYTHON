import pygame
import sys

pygame.init()

screen_surf = pygame.display.set_mode(size=(800,640))
print(screen_surf.get_rect())
ship_img_surf=pygame.image.load('images/ship.bmp').convert()
print(ship_img_surf.get_rect())
alien_img_surf=pygame.image.load('images/alien.bmp')
font = pygame.font.SysFont(None,64)
font_surf=font.render(
                    str(5678),
                    True,
                    (0,0,0)
                    )
print(font_surf.get_rect())

bullets = []
aliens = []

bullet_rect = pygame.Rect(0, 0, 10, 50)
bullets.append(bullet_rect)    #리스트 안에 bullet_rect 객체의 참조(pygame.Rect(0, 0, 10, 50)) 를 리스트에 저장하는 것. bullet_rect 자체가 아니라!
print(bullet_rect)
print(bullets)

clock = pygame.time.Clock()

#events in list
#events= []
#events 리스트는 pygame.event.get()을 호출하여 생성된 많은 모든 이벤트 객체들의 리스트임
#키보드 마우스 조이스틱..(사용자 입력)같은거랑 시스템 이벤트들임
#events[0]이라고 하면 제일처음저장된 pygame.event.Event 객체!
while True:
     events=pygame.event.get() # 이벤트를 한 번만 가져옵니다
     for e in events:
          print(e.type, type(e.type)) #현재 이벤트 큐에 있는 모든 이벤트를 출력
          if e.type == pygame.QUIT:  # pygame.QUIT 이벤트는 창을 닫는 이벤트입니다.
               #print('QUIT')
               sys.exit()
          elif e.type == pygame.KEYDOWN: 
               pass #pass는 파이썬에서 아무 작업도 하지 않는 코드 블록
               #print('KEYDOWN')
               #print(e.key)               
          elif e.type == pygame.KEYUP: 
               # print('KEYUP')
               #print(e.key)
               if e.key == pygame.K_SPACE: #스페이스 누르면 종료.
                    sys.exit() # 프로그램 종료

     screen_surf.fill('white')
     screen_surf.blit(ship_img_surf, ship_img_surf.get_rect())
     screen_surf.blit(font_surf, (100,100)) #font_surf는 이미 font.render() 함수를 통해 생성된 텍스트 이미지. 폰트라기보다는 폰트를가진 이미지
     pygame.display.flip()
     clock.tick(60)

