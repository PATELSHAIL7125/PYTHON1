# SHOPPING CART PROGRAM 

foods = []
prices = []
total = 0

while True:
   food = input("Enter the food item (q to quit): ")
   if food== "q":
      break
   else:
      prices += float(input("Enter the {food} price: "))
      foods.append(food)
