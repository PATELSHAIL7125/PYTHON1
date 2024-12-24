#LIST COMPREHENSION =  a concise way  to create lists in python 
#  compact and easier to read than traditional loops 
#  [expression for value in iterable if condition]

doubles = []

for x in range (1,11):
    doubles.append(x*2)

print(doubles)

# Write in shgort form using list comprehension

doubles = [x*2 for x in range(1,11)]
triples = [y*3 for y in range(1,11)]

print(doubles)
print(triples)

fruits = ["apple","banana","cherry","kiwi","mango"]
uppercase = [fruit.upper() for fruit in fruits]
print(uppercase)

