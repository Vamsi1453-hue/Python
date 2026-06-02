#check month based on input number
month=int(input("Enter month number: "))
if(month>=1 and month<=12):
    print(month,"is valid month.")
else:
    print(month,"is invalid month.")