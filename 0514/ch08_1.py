import random

a =[]
n =0

while n<6:
     b=random.randint(1,45)
     a.append(b)
     n = n+1

print(a)

#a라는 빈리스트 만들어주고 n은 0인 채로
#n이 0이니까 이것부터 반복문 실행하면
#b는 1부터 44까지 중 랜덤숫자 하나가 만들어지고 a에 그것이 추가되고
#n이 하나 커진채로 다시 반복문을 올라가니까
#n이 0일때 a에 리스트 하나 추가되고, n이 1일때 리스트 하나 추가되고
#순서대로 하나씩 추가되는걸 이해하면됨 

matrix=[]

for _ in range(3):
     row=[]
     for num in range(1,4):
          row.append(num)
     matrix.append(row)

matrix=[]

for _ in range(2):
     row=[]
     for num in range(5,8):
          row.append(num)
     matrix.append(row)
     
     print(row)

fruits = []
for _ in range(3):
     fruit = input("Enter a fruit:")
     fruits.append(fruit)
print(fruits)