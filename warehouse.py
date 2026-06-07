'''list1=list(map(int,input("Enter first list").split()))
list2=list(map(int,input("Enter second list").split()))
listFinal=[]
listFinal=list1+list2
print(listFinal)
listFinal.count()
print(listFinal)
'''
Godown_A=list(map(str,input('Enter the product codes: ').split()))
Godown_B=list(map(str,input('Enter the product codes: ').split()))
print('Unified Inventor: ',set(Godown_A+Godown_B))
#pending of count