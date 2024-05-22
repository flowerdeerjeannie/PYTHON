import matplotlib.pyplot as plt
from bug import RandomWalk
#from 모듈 import 클래스

#RandomWalk 클래스의 객체 생성 (rw) 및  객체 메소드 호출-
#fill_walk() 메서드는 랜덤한 좌표들을 계산하고, rw 객체의 x_values와 y_values 리스트에 이를 저장함
#프로그램이 실행중이면 계속 랜덤워크 새로 만들기 위해 무한반복ㄷ문 while True 사용
while True:
    rw = RandomWalk(rows=10, cols=10)
    x_values, y_values = rw.fill_walk(num_points=5000, x_start=5, y_start=5)
    point_numbers = range(len(x_values))

    plt.style.use('classic')
    fig, ax = plt.subplots()

    ax.bar(x_values, y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
    ax.set_aspect('equal')
    plt.show()

    keep_running = input("Make another walk? (y/n):")
    if keep_running == 'n':
        break