with open("example.txt",encoding='utf-8') as file:
  data = file.read()
  print(data)

import os
directory = os.getcwd()
flist = os.listdir(directory)
print(flist)