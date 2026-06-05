Stu={
    101:'scott',102:'miller',103:'adams',104:'james',105:'danish'
}
print(Stu)
print(Stu.values())
print(Stu.keys())
Colors={
    
}
keys=[101,102,103]
values=('red','green','blue')
print(Colors.fromkeys(keys,values))
print(Stu.get(101))
print(Stu.get(103))
print(Stu.items())
print(Stu.update({103:'blue'}))
print(Stu.pop(101))
print(Stu.popitem())
print(Stu)
Stu.setdefault(107,'Null')
print(Stu)
#nested list
List=[[10,20,30],[40,50,60],[70,80,90]]
for i in List:
    print(i)
#nested tuple
Tuple=((1,2,3),(4,5,6),(6,7,8))
for i in Tuple:
    print(i)