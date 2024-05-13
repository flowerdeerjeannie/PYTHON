alien_0={}

alien_0['color']='green'
alien_0['points']='5'
alien_0['x_position']=0
alien_0['y_position']=25
alien_0['speed']='medium'
print(alien_0)

# alien_0['color']='yellow'
# print(alien_0)

# if alien_0['speed'] == 'slow':
#      x_increment = 1
# elif alien_0['speed'] == 'medium':
#      x_increment = 2
# else :
#      x_increment = 3

# alien_0['x_position']=alien_0['x_position']+x_increment
# print(f"new position={alien_0['x_position']}")

del alien_0['color']
print(alien_0)

for key,value in alien_0.items():
     print(f"{key}:{value}")

aliens=[]
for alien_number in range(30):
     new_alien={'color':'green', 'points':5,'speed':'low'}
     aliens.append(new_alien)
print(aliens)

for alien in aliens[:3]:
     if alien['color'] =='green' :
          alien['color'] = 'yellow'
          alien['speed'] = 'medium'
          alien['points'] = 10

for alien in aliens[:5]:
     print(alien)
print("...")