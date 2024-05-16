class Car2:
     
     def __init__(self, make, model, year):
          self.make = make
          self.model = model
          self.year = year
          self.odometer_reading = 0
          #얘는 인자값 안받아도 인스턴스에 항상 0으로 생성되는거
     
     def get_descriptive_name(self):
          #return 뱉을때 그 값을 구성하기 위한 임시변수 long_name
          long_name = f"{self.year} {self.make} {self.model}"
          return long_name.title()
     
     def read_odometer(self):
          print(f"{self.odometer_reading}")

     def fill_gas_tank(self):
          print("기름을 채워주십사")


class Battery:

     def __init__(self, battery_size=40):
          self.battery_size= battery_size
     
     def describe_battery(self):
          print(f"this car has {self.battery_size} of battery.")



     
class ElectricCar(Car2):
     """"Car2를 슈퍼클래스로 상속받아 ElectricCar클래스 만듦 """
     def __init__(self, make, model, year):
          super().__init__(make, model, year)
          self.battery = Battery()

     def fill_gas_tank(self):
          super().fill_gas_tank()
          print("but this car doesn't have a gas tank")
          


my_leaf=ElectricCar('nissan','leaf',2024)
print(my_leaf.get_descriptive_name())
my_leaf.fill_gas_tank()
my_leaf.battery.describe_battery()

#메소드까지 상속받기때문에 오버라이드 할거아니면 메소드전달없이 init만 작성해줘도
#메소드 및 필드 다쓸수있음. 




my_new_car = Car2('audi','a4',2024)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()

#인스턴스 속성값 수정법
my_new_car.odometer_reading = 23



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"

# Person 객체 생성
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# __str__() 메서드 호출하여 문자열로 변환
print(person1)  # 출력: Name: Alice, Age: 30
print(person2)  # 출력: Name: Bob, Age: 25


#str 같은 __자동출력__메소드를 사용하면
#person1.str 이라고 하지 않아도 자동으로 저 값이 출력된다. 