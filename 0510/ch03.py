# data = [1,2,3]
# print(data,type(data))

# # data = list ()
# # print(data, type(data))

# print(data[0])
# print(data[1])
# print(data[2])


# data.append(6)
# data.append(7)
# data.append(8)
# print(data, len(data))

# data[3] = 4
# data[4] = 5
# print(data, len(data), sum(data), min(data), max(data))



# data = list(map(int,input().split()))
# print(data, type(data), type(data[0]))
# print(sum(data))

# data = [1,2,3]
# del data[1]
# print(data)

# data = input()
# print(data.split())

# data = [ 1, 2, 3.14, 'hello', len, range(5)]
# print(data, type(data))
# for a in data:
#      print(a, type(a))

# msg = 'aba'
# print(msg == msg[::-1])

data=[2,5,1,3,5]
print(data[-1])
print(data[::-1])
print(data[-2])
print(data[3])

data.append(6)
print(data)
data.pop()
print(data)
data.insert(6,6)
print(data)

del data[1]
print(data)

print(sorted(data))