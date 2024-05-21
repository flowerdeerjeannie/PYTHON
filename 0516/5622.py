
S=input()
time=0

list = {"abc":3, "def":4 , "ghi":5, "jkl":6, "mno":7, "pqrs":8, "tuv":9, "wxyz":10}


for i in S:
     for k,v in list.items():
          if i in k:
               time += v
               break

print(time)
