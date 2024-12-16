# LOGICAL OPERATOR 

# Logical operators are used to combine conditional statements: 
# and, or, not (EVALUATE THE MULTIPLE CONDITION IN A SINGLE LINE) 

# AND - Returns True if both statements are true
# OR - Returns True if one of the statements is true
# NOT - Reverse the result, returns False if the result is true

temp = 35;
is_raining =True 

if temp >35 or temp < 0 or is_raining:
    print("stay at home")
else:
    print("go out and have fun")

# NOT - Reverse the result, returns False if the result is true

if not is_raining:
    print("go out and have fun")
else:
    print("stay at home")
    