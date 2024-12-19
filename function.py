#  function = A BLOCK OF REUSABLE CODE
#   PLACE()  AFTER THE FUNCTION NAME TO INVOKE IT   

# to define the function use the keyword def 

def greet_user():
    print("hi enter to the department")


greet_user();

# argument function 
def birthday(name):
    print(f"happy birthday {name}")

birthday("Riya")


# return = statement used to end a function and 
      # send a result back to the caller  
    
def add(a,b):
    return a+b

result = add(2,3)
print(result) 