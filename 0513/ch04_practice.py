plist = ['peperoni', 'bulgogi', 'combination']
for i in plist:
     print(f"i like {i} pizza.")
     print(f"i really love my Dear {i} pizza.\n")

data = ['tiger','lion','bear', 'rabbit', 'bambi']
for d in data:
     print(f"The {d} is the really great animal to live together.")
     print(f"The {d} have good tails.\n")

t = [ 1, 5, 7, 33, 39, 62]
for p in enumerate(t):
     print(p)

numbers = list(range(1,1001))
print(numbers)

print(min(numbers))
print(max(numbers))
print(sum(numbers))
print(sum(range(1,1001))/len(range(1,1001)))

array = list(range(1,20,2))
print(array)

print([i*3 for i in range(1,11)])


array_3 = [i**3 for i in range(1,11)]
print(array_3)

print(f"리스트의 첫 세 항목은 {data[:3]}")
print(f"중간은 {data[1:3]}")
print(data[2:])

friend_plist = plist[:]
print(friend_plist)
plist.append('delicious')
print(plist)
friend_plist.append('cheese')
print(friend_plist)
