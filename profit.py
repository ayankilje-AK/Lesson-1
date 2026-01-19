actual_cost = float(input("Enter the actual cost of the product"))
sales_price = float(input("Enter the price at which you sell the product"))

if (sales_price > actual_cost):
    amount = (sales_price - actual_cost)
    print("Total profit = {0}". format(amount))
else:
    print("NO PROFIT!!!")