Stu={
    101:'scott',102:'miller',103:'adams',104:'james',105:'danish'
}
print(Stu)
Stu[102]='cbt'
print(Stu)
del Stu[103]
print(Stu)
#check 101,104,105
print(101 in Stu)
print(104 in Stu)
print(105 in Stu)
print(103 not in Stu)
print(102 not in Stu)
print(Stu)
print(Stu.values())
print(Stu.keys())