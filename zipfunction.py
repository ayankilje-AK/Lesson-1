s1 = {2, 3, 1}
s2 = {"B", "A", "C"}
result = list(zip(s1, s2))
print(result)

l1 = [1, 2, 3]
l2 = [102, 103, 104]

for x,y in zip(l1, l2[::-1]):
    print(x, y)

stock = ["Reliance", "Infosys", "TCS"]
prices = [23000, 12000, 2340]
result = {stock : prices for stock, prices in zip(stock, prices)}
print('\n{}'.format(result))
