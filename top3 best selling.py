def top_three_sales(sales):
    sorted_sales = sorted(sales, reverse=True)
    return sorted_sales[:3]

sales1 = [450, 120, 890, 330, 760, 210]
print("Top 3:", top_three_sales(sales1))

sales2 = [50, 60, 70, 80]
print("Top 3:", top_three_sales(sales2))
