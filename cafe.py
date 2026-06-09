class Employee:
    def __init__(self,eid,name):
        self.eid=eid
        self.name=name
class FoodItem:
    def __init__(self,name,price):
        self.name=name
        self.price=price
class Order:
    def __init__(self):
        self.items=[]
    def add_item(self,item):
        self.items.append(item)
    def bill(self,emp):
        total=sum(i.price for i in self.items)
        print("-"*50)
        print(f"Employee ID: {emp}")
        print(f"Employee name: {emp}\n")
        print("-"*50)
        print("Item\t\tprice")
        for i in self.items:
            print(f"{i.name} {i.price}")
        print("-"*50)
        print(f"Total Amount :{total}")
        print("payment status : Paid")
        print("-"*50)
emp=Employee('E123','scott')
Order=Order()
Order.add_item(FoodItem("coffee",40))
Order.add_item(FoodItem("sandwich",80))
Order.add_item(FoodItem("Brownie",60))
Order.bill(emp)        