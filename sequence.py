# sequence types in python
#Lists are mutable
Lang=['Java','Python','C++']
print(Lang)
print(type(Lang))
#Tuples are immutable
Lang=('Java','Python','C++')
print(Lang)
print(type(Lang))   
#Sets are unordered collection of unique elements
Lang={'Java','Python','C++'}
print(Lang) 
print(type(Lang))
#Strings are immutable sequence of characters
Str1='Hello, World!'
print(Str1)
print(type(Str1))
str2="It can span multiple lines"
print(str2)
print(type(str2))
Str3='''This is a multi-line string.'''
print(Str3) 
print(type(Str3))
Lang={101:'Java',102:'Python',103:'C++'}
print(Lang)
print(type(Lang))
a=True
print(a)
print(type(a))

print(True+True)
#range(start, stop, stepsize)
range1=range(1,10)
print(range1)
print(type(range1))
for i in range1:
    print(i)