from random import choice

class RandomWalk: #랜덤 워크의 기본 포인트숫자는 5,000
     def __init__(self, num_points=5000):
          self.num_points=num_points
          #x,y값을 저장할 리스트를 만들고 원점 (0,0) 으로 초기화
          self.x_values = [0]
          self.y_values = [0]

     def fill_walk(self):
          #설정한 이동 수에 도달할때까지 움직임 반복
          while len(self.x_values) < self.num_points:
               #좌우 방향을 정하고 1은 오른쪽, -1은 왼쪽!
               #choice 함수는 주어진 리스트에서 임의의 요소를 반환하는 랜덤 반환 함수!!!
               x_direction = choice([1,-1])
               #얼마나갈지 정한다. 이동할 거리! 0은 수직이동
               x_distance = choice([0,1,2,3,4])
               x_step = x_direction * x_distance

               y_direction = choice([1,-1])
               y_distance = choice([0,1,2,3,4])
               y_step = y_direction * y_distance

               #다 0,0 으로 움직임이 없을땐 무시하고 컨티뉴한다 
               if x_step == 0 and y_step == 0:
                    continue

               #새 위치를 계산한다. x_values의 마지막 값에 x_step 하나를 더해 다음 x값을 결정하고 그거를 밑에 추가한다. 
               #x_values[-1]은 인스턴스 변수의 x_values리스트의 마지막 요소를 의미함.
               #x는 x가 움직이는 점. 자리들. x좌표.
               x = self.x_values[-1] + x_step
               y = self.y_values[-1] + y_step

               self.x_values.append(x)
               self.y_values.append(y)


#x_values는 하나의 값이 아니고 X의 계속적인 랜덤한 움직임을 다 기록하는거니까 list형태임을 알고 볼것