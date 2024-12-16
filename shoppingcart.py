item = input(" what item would you like to buy?")
price = float(input("what is the price of the item?"))
quantity = int(input("how many would you like to buy?"))
total = float(price*quantity)

print(total);

print(f"you have bought {quantity} {item} and your total amount is ${total}")

