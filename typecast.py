# TYPECASTING -  THE PROCESS OF CONVERTING A ONE DATA TYPE INTO A ANOTHER DATA TYPE 
#  str() , float() , int() , bool()

name = "BRO CODE "
age = 25
gpa = 3.2
is_student = True;
 
gpa = int(gpa)# its convert the float into a integers 
print(gpa)
  
age = str(age)# its convert the integer into a string
age+="11";# 2511 is ans bcz age is string
print(age)

# real life example

name= bool(name)# its convert the string into a boolean
print(name)# its print true bcz name is not empty string
#if string is empty then it print false


