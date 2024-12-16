#collection = Single "variable" used to store multople values 
# LIST   = [] ORDERES AND CHANGABLES  DUPLICATES OK
# SET    = {}  UNORDERED AND IMMUTABLE , BUT ADD/REMOVE OK. DUPLICATES NO
# TUPLE  = ()  ORDERED AND UNCHANGABLES, DUPLICATES OK FASTER 

fruit = ["apple", "banana", "cherry"]  # THIS IS A LIST
# print(fruit)


# for accessing the elements in the list
print(fruit[0:3:2])  # apple 

# accesing with the for loop 

for x in fruit:
    print(x) 

print(dir(fruit))  # to see the methods that can be used with the list
print(help(fruit))  # to see the methods that can be used with the list with its description