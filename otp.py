m=list(str,input("Enter your msg:").split())
for i in m:
    if i.isdigit() and len(i)==6:
        print(i) 