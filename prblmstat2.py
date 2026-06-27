def merge_inventory():
    n = int(input("Enter number of items: "))
    inventory = {}

    for _ in range(n):
        item, qty = input("Enter item and quantity: ").split()
        qty = int(qty)
        if item in inventory:
            inventory[item] += qty
        else:
            inventory[item] = qty

    print("Merged Inventory:")
    for item, qty in inventory.items():
        print(item, qty)


merge_inventory()
