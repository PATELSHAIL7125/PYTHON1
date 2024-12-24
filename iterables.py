#ITERABLES = AN OBJECT/COLLECTION THAT CAN RETURN ITS ELEMENT ONE AT A TIME 
#ALLOWING IT TO BE ITERATED OVER IN A LOOP 

numbers = [1, 2, 3, 4, 5, 6]

for number in numbers:
    print(number,end="-")

fruites = {"apple","banana","cherry"}

for fruit in fruites:
    print(fruit,end="-")

dictionario = {"name":"John","age":25,"city":"New York"}

for key,value in dictionario.items():
    print(f"{key}={value}",end="-")