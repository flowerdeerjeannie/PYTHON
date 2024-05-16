#https://codermun-log.tistory.com/73







class Dog2:
     """클래스 Dog 정의"""

     #인스턴스 만들때 Dog클래스 기반으로 자동 실행하는 메서드, (self)는 필수로 자동전달되는 것임. 인스턴스자체
     #Dog의 인스턴스를 만들면 파이썬이 아래 init을 호출하며 name, age를 전달함 
     #INIT은 인스턴스 변수, 모두 같은 값이 아니고 각 인스턴스가 개별적으로 가짐
     def __init__(self, name, age):
          self.name = name
          self.age = age
     ### 클래스   안에서 속성에 접근할때는 {self.속성}
     def sit(self):
          """동작메서드"""
          print(f"{self.name}이 앉는다.")

myDog = Dog2("hong", 10)
#myDog은 인스턴스, Dog2는 클래스이고 ()는 인자값 

# 클래스 바깥에서 속성에 접근할때는 인스턴스.속성 형식
myDog.sit()






#위치인수 사용법
class Person:
    #인수가 []배열 리스트로 전달이 될때 *표시를 해주고
    #리스트를 풀어서 전달하기 위해 *args를 사용
    def __init__(self, *args):
        self.name = args[0]
        self.age = args[1]
        self.address = args[2]

maria = Person(*['마리아', 20, '서울시 서초구 반포동'])


#[]는 args로, {}딕셔너리는 kwargs로 통칭한다고 생각하면됨 


#키워드인수 사용법
class Person:
    # 키워드 인수와 딕셔너리 언패킹을 사용하려면 **kwargs를 사용 
    def __init__(self, **kwargs):    
        self.name = kwargs['name']
        self.age = kwargs['age']
        self.address = kwargs['address']

maria1 = Person(name='마리아', age=20, address='서울시 서초구 반포동')
maria2 = Person(**{'name': '마리아', 'age': 20, 'address': '서울시 서초구 반포동'})