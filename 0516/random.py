
from typing import Any

# print(randint(1,6))



class Student:
     count=0
     #count는 해당 클래스의 모든 인스턴스에서 공유되는 클래스 변수임
    
     def __init__(self):
          Student.count += 1 #클래스 변수 count를 1씩 증가시키는거
          #self.count 라고 적게 되면 각 인스턴스마다의 count, 각 인스턴스마다 고유한 값을 가지게 되는거고
          #Student.count 라고 해줘야 해당 클래스의 모든 인스턴스에서 공유하는것임
          # self.count는 인스턴스 변수를 변경하는 것이므로 해당 인스턴스의 값만 변경되고, 
          #다른 인스턴스나 클래스 변수에는 영향을 주지 않습니다.

print(f"{Student.count}")
s = Student()
#Student 클래스의 인스턴스를 생성하여 변수 s에 할당. 객체가 아니고 번지 가지는 참조변수임
# s는 Student클래스의 객체를 참조하게 하는 참조변수임
print(f"{Student.count}")

def initialize():
     return 1,2,3

_,_,b = initialize() #첫번째 두번째 값을 무시하고 세번째 값만 b에 할당.

a=[1,2,3]
b=[4,5,6]
mergeList = [*a,*b] # 기호 *를 사용하여 리스트를 unpack 하고 merge하는거임
print(mergeList)


#인덱싱 구현
class MyList:
     def __init__(self,data):
          self.data = data

     #인덱스를 받아서 해당 인덱스의 값을 반환하는 메서드!!!
     def __getitem__(self, index):
          return self.data[index]

mlist = MyList([1,2,3,4])
print(mlist[1:3]) #인덱스 1부터 인덱스 2까지 요소를 슬라이싱하여 반환함.
#이때 __getitem__메소드가 자동으로 호출되는거지 

s= ['s1','s2','s3']
num= [5, 3, 7]
#zip(a,b)를 통하여 객체 간 인덱스 !!위치가 같은 것끼리!! 묶어서 튜플로 반환함
# score를 리스트로 변환하여 출력하여야 함
score = list(zip(s, num))
print(score)

# 리스트로 변환한 score를 반복하여 출력
for a, b in score:
     print(f"[{a},{b}]")