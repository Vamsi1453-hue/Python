#shallow copy
import copy
original=[1,2,3,4,5]
print(original)
new=original
print(new)
new[0]=100
print(original)
print(new)

