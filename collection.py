#collection = Single "variable" used to store multople values 
# LIST   = [] ORDERES AND CHANGABLES  DUPLICATES OK
# SET    = {}  UNORDERED AND IMMUTABLE , BUT ADD/REMOVE OK. DUPLICATES NO
# TUPLE  = ()  ORDERED AND UNCHANGABLES, DUPLICATES OK FASTER 

fruit = ["apple", "banana", "cherry"]  # THIS IS A LIST
# print(fruit)


# for accessing the elements in the list
print(fruit[0:3:2])  # apple 

# accesing with the for loop 

for fruits in fruit:
    print(fruits) 

# print(dir(fruit))  # to see the methods that can be used with the list
# print(help(fruit))  # to see the methods that can be used with the list with its description

#in operator 
 
print("apple" in fruit)  # ANS IS IN BOOLEAN TRUE

#CHANGE THE VALUE OF THE LIST
fruit[0] = "orange"
print(fruit)  # ['orange', 'banana', 'cherry']

#APPENDD THE ELEMENT IN THE LIST

fruit.append("mango") 

# REMOVE THE ELEMENT FROM THE LIST

fruit.remove("banana")
print(fruit)  # ['orange', 'cherry', 'mango']

# INSERT THE ELEMENT IN THE LIST

fruit.insert(1, "banana") 

#sort method in the list 

fruit.sort()

#reverse method in the list

fruit.reverse() 

#fruit.clear()  # to clear the list

print(fruit.index("mango"))  # to get the index of the element

print(fruit.count("banana"))  # to get the count of the element

# COPY THE LIST

fruit2 = fruit.copy()




#############    SETS    ####################


# SETS ARE UNORDERED AND UNINDEXED AND NO DUPLICATES

fruit = {"apple", "banana", "cherry"}

print(fruit)  # unoredered print 

#pop method in the set

fruit.pop()  # it will remove the random element from the WHICH WILL BE REMOVED




#############  TUPLES    ####################

# TUPLES ARE ORDERED AND UNCHANGABLES AND ALLOW DUPLICATES

# tuples are faster than the other 

# we have limited methods in the tuples

fruit = ("apple", "banana", "cherry")

print(fruit)  # ('apple', 'banana', 'cherry')

#index method , count method and length method are used in the tuples 
