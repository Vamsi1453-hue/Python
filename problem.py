#use loop or direct input to populate the list with 7 numbers and use sum() to get total , max() for best day , min() for worst day and store each input in float or int format, not string
n=7
Revenue=[]
for i in range(1,8):
    element=int(input(f"Enter the revenue for day{i}: "))
    Revenue.append(element)
print(f"Total Revenue :{sum(Revenue)} | Best Day:{max(Revenue)} | Worst Day:{min(Revenue)}")

#another logic for code
Revenue=list(map(int,input("Enter the Revenue for 7 days").split()))
print(f"Total Revenue:{sum(Revenue)} | Best Day: {max(Revenue)} | Worst Day: {min(Revenue)}")