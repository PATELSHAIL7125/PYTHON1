# dictionary  =  a collection of {key:value} pairs
#  ORDERED CHANGABLE AND NO DUPLICATES 

capitals = {"INDIA":"NEW DELHI",
            "USA":"WASHIGTON DC"}

# FOR ACCESSING THE ELEMENGTS USE GET METHOD

print(capitals.get("INDIA")) # NEW DELHI

#UPDATE METHOD (INSERT NEW KEY VALUE PAIR OR UPDATE THE EXISTING VALUE) 

capitals.update({"UK":"LONDON"})

# TO REMOVE THE KEY VALUE PAIR 

capitals.pop("USA")

#POP ITEM REMOVES THE LAST ITEM OF THE DICTIONARY

capitals.popitem()

# clear method removes all the items from the dictionary

#capitals.clear()

#KEYS METHOD 

keys=capitals.keys()  # USA INDIA UK GERMANY 
print(keys)

#VALUES METHOD 

values = capitals.values() # WASHINGTON DC NEW DELHI LONDON BERLIN
print(values)

#ITEMS METHOD

items = capitals.items() # USA WASHINGTON DC 
print(items)#dict_items([('INDIA', 'NEW DELHI')])   it gives 2D list of tuples 

for key,values in capitals.items():
    print(key,values)
    