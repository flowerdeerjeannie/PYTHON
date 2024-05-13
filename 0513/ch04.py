# data = [ 1, 2, 3]

# for d in data:
#      print(d, end=' ')
# data[1]=5
# # 이렇게 했더라도 실제 배열이 변경되는것은 아님. data[1]을 출력하면 5로 나오지만 값이 변경되지는 않는다. 
# print(data[1])
# # 문자열에 for를 돌려도 그냥 쪼개주는군 
# string='hello'
# for s in string:
#      print(s, end=' ')

# print('-',string[1])
# # 진짜배열은 값을 변경가능하지만 string type은 변경불가함 


# print(data, type(data))
# data2 = [i** 2 for i in data if i**2<26]
# # 그 배열에 함수넣어 값의 새로운배열가능 
# print(data2)

# nums = [1,2,3,4]
# nums.insert(-1,'h')
# print(len(nums))

data = (1, 2, 3)
print(data, type(data))
for i in data:
    print(i)
#data[1] = 5

# data2 = [i**2 for i in data if i**2 < 5]
# print(data2, type(data2))

data3 = []
for i in data:
    if i**2 < 10:
        data3.append(i**2)
print(data3)

data3 = [i**2 for i in data if 5<i**2 <20 ]
data3.append(i**2)
print(data3)

for i in range(10):
    print('i',end=' ')

for i in range(10):
    print(i,end=' ')

for idx, d in enumerate(data):
    print(idx, d)

squares = []
for value in range(1,11):
    square = value**2
    squares.append(square)
print(squares)
# //for돌리고 빈배열에 끝에 추가하는것처럼 생각할때는
# 임시변수 sqare를 만들어서 해준거고
# 아니면 
squares=[]
for value in range(1,11):
    squares.append(value**2) 
print(squares)
#     라고만 해주면 됨  

data_2d = [[1,2,3] , [4,5,6]]
for data in data_2d:
    for d in data:
          print(d, end=' ')

# for i in range(1,10):
#      for n in range(1, 10):
#          print(f"{i}*{n}={i*n}")

# for a in range (1,11):
print(sum(range(1,11)))
print(min(range(1,11)))
print(max(range(1,11)))

numbers=[]
for value in range(1,10):
     numbers.append(value**2)
print(numbers)

data = list(range(1,11))
print(data, data[0:5], sep='\n')
# spe='\n'은 ()안에서 콤마뒤에 엔터해줌
print(data, data[-1], sep='\n')
print(data[:5],data[5:])
print(data[::-1])

# 배열은바뀌어 [] 튜플은안바뀌어 ()
data = [1,2,3]
data2 = data[:]
data2[1]=5
print(data, data2)