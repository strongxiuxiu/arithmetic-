from itertools import chain

a = [1,3]
b= [5,6]
d= [333]
cv = chain(a,b,d)
print(cv)
for item in cv:
  print(item)


acc = a | b
print( )
