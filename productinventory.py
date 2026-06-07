#A warehouse management system tracks stock quantities in a dictionary. When goods arrive, the stock count increases. When an order ships, it decreases. Update the stock dictionary based on a list of transactions: each transaction is a tuple (product_id, quantity, type) where type is 'IN' or 'OUT'.
stock = {}
for pid, qty, typ in [("P1",10,"IN"),("P2",5,"IN"),("P1",3,"OUT")]:
    stock[pid] = stock.get(pid,0) + (qty if typ=="IN" else -qty)
    stock[pid] = max(stock[pid],0)
print(stock)

