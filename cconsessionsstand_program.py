# cconsession stand program 

menu = {"pizza":3.00,
        "nachos":2.00,
        "hotdog":1.50,
        "popcorn":6.00,
        "fries":2.50,
        "chips":1.00,
        "soda":3.00,
        "lemonade":2.00,
        }

cart = [];# it make a list for adding the user selected items 
total=0;

for key,values in menu.items():
    print(f"{key:10}:{values:.2f}")

while True:
    food = input("Enter the food item you want to order(q to quit): ")
    if  food == "q":
        break;
    elif  menu.get(food):
        cart.append(food)
        

for food in cart:
    total = total+menu.get(food)
  
print(f"Your total bill is {total:.2f}")