#check number of days in a month
month=int(input("Enter month number: "))
if(month in [1,3,5,7,8,10,12]):
    print("31 days in this month.")
elif(month in [4,6,9,11]):
    print("30 days in this month.")
elif(month==2):
        print("29 days in this month.")
else:
    print("Invalid month number.")