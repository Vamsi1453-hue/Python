#string operations
Str="           This is a string example"
print(Str.capitalize())
print(Str.casefold())
print(Str.count('i'))
print(Str.encode())
print(Str.center(29,"*"))
print(Str.endswith('e'))
print(Str.expandtabs(tabsize=3))
print(Str.find('a'))
print(Str.format(10,"*"))
#scott@oracle
Str="scott@oracle.in"
a=Str.find('@')
d=Str.find('.')
print(Str[0:a])
print(Str[a+1:d])
print(Str.isascii())
