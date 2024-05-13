names = ['kim','lee','kang']
for i in names:
     print(i,type(i))
     print(f"{i}, you can count on me")

cars = ['porsche', 'car', 'car2', 'car3']
print(f"I really wanna get {cars[0]} cayenn.")

guests = ['Barbie','Ken','Dumbass']
for name in guests:
     print(f"i'll invite {name}! ")

print(guests[2])
del guests[2]
print(guests)
guests.insert(0,'Jeannie')
print(guests)
for a in guests:
     print(f"i'll invite {a}! ")

guests.append('ini')
print(guests)
guests.insert(1, 'mini')
print(guests)
guests.insert(0, 'mo')
print(guests)
for name in guests:
     print(f"Im really sorry but you can come here for just two. please come to my house {name}")
guests.pop()
print(guests)
guests.pop()
print(guests)
guests.pop(1)
print(guests)