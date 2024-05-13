car = 'subaru'
print("Is car == 'subaru'?I predict true.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

print(car == 'subaru')
print(car != 'subaru')

data = [1,2,3]
if 3 in data:
     print(data[-1])

print(len(data)>2)
print(len(data)>3)

print(sum([True, True, False, 3, 5, True, False]))

if 1<2 :
     print("aaa")
if 1-1 :
     print("aaa")

alien_color = 'red'
if alien_color == 'green':
     print("the player has got 5 points")
elif alien_color == 'yellow':
     print("the player has got 10 points")
else: 
     print("you got 15 points")

age = 3
if age < 2:
     print('baby')
elif (age < 4):
     print('toddler')
elif (4 <= age ) and (age < 13):
     print('kid')
elif 65 < age :
     print('elder')


favourite_fruits = ['strawberry', 'applemango', 'pineapple']
if 'strawberry' in favourite_fruits:
     print (f"you really love strawberry")
if 'applemango' in favourite_fruits:
     print (f"you really love applemango")
if 'pineapple' in favourite_fruits:
     print (f"you really love pineapple")


data = [1,2,3]
for d in data:
     if d <2:
          print(d)
     else:
          print('wrong')

user = ['ini','admin','mini','myni','mo']
new = ['mini','myni', 'lee', 'kim', 'park']
for i in user:
     if i == 'admin':
          print("관리자님상태보고서")
     else:
          print(f"{i}님, 다시로그인감사 ")

for id in new:
     if id in user:
          print(f" {id},새 사용자 이름을 입력하세요")
     else:
          print(f" {id},ㄱㄴ")
          
useruser = [id.lower() for id in user]
print(useruser)
for id in useruser:
     if id in new:
          
          print(f"{id}야 중복이구나")
     else:
          print("null")