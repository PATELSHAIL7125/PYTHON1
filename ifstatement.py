#if = Do some code if some condition is true
#else = Do some code if some condition is false

age = int(input("what is your age?"))

if age >= 18:
    print("you are an adult")
else:   
    print("you are not an adult") 
# elif = else if

if age >= 18:
    print("you are an adult")
elif age >= 13:
    print("you are a teenager")
else:
    print("you are a child")

# condition baased 

is_student = True
if is_student:
    print("Yes you are a student")
else:
    print("No you are not a student")
    