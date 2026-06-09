class Employee:
    def __init__(s,i,n): s.id=i; s.name=n

class FoodItem:
    def __init__(s,n,p): s.name=n; s.price=p

class Order:
    def __init__(s,oid): s.id=oid; s.items=[]
    def add_item(s,item): s.items.append(item)
    def total(s): return sum(i.price for i in s.items)
    def bill(s,e):
        print("CORPORATE CAFETERIA BILL")
        print("ID:",e.id,"\nName:",e.name)
        print("-"*30)
        for i in s.items:
            print(i.name,"- rs",i.price)
        print("-"*30)
        print("Total: rs",s.total())
        print("Status: PAID")

class Cafeteria:
    def __init__(s): s.menu=[]
    def add_food_item(s,item): s.menu.append(item)

e=Employee("E101","Ryan")
coffee=FoodItem("Coffee",40)
sandwich=FoodItem("Sandwich",80)
brownie=FoodItem("Brownie",60)

c=Cafeteria()
for i in [coffee,sandwich,brownie]: c.add_food_item(i)

o=Order("O101")
for i in [coffee,sandwich,brownie]: o.add_item(i)

o.bill(e)