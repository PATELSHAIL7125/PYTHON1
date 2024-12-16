#2D LIST IN PYTHON 

fruits = ["apple","bananna","ornage","coconut"]
vegetables = ["potato","tomato","onion","carrot"]
meats  = ["chicken","mutton","turkey","fish"]


grocieries = [fruits,vegetables,meats]
print(grocieries)  # [['apple', 'bananna', 'ornage', 'coconut'], ['potato', 'tomato', 'onion', 'carrot'], ['chicken', 'mutton', 'turkey', 'fish']]
 
# for accessing the elements in the list

grocieries[0] = ["apple","bananna","ornage","coconut"]
grocieries[1] = ["potato","tomato","onion","carrot"]
grocieries[2] = ["chicken","mutton","turkey","fish"]

# grocieries[0][0] = "apple"
# grocieries[0][1] = "bananna"
# grocieries[1][1] = "tomato"

#ITERARTING IN THE 2D LIST

for item in grocieries:
   for i in item:
        print(i)