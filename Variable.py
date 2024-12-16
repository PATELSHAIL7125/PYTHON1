#- this is use to comment code in python 

  # variable -  A container for a value (string , integer, float, boolean) it behavce like the it containe thhe value 
 # variable names are case-sensitive (name, Name and NAME are different variables)   
 
first_name = "BRO"

print(first_name)

#  BUT PRINT IN DIFFRENT WAY USE THIS METHOD 
 
print(f"hello {first_name}" )

food = "pizza"
print(f"hello {first_name} do you like {food} ")



#INTEGER - whole number

age = 25
print(f"your age is {age}")

#float 

price = 10.99;
print(f"the price is ${price}")
gpa =  3.2
print(f"your gpa is {gpa}")


#BOOLEAN - True/False
is_student = True
print(f"Are you a student? : {is_student}")


#if and else statement 
if is_student:
    print("Yes you are a student")
else:
    print("No you are not a student")
 

 #type function - returns the data type of the variable

print(type(first_name))
print(type(age))
print(type(price))