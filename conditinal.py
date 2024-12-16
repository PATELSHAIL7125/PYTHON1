#conditional expression - a ternary operator that returns a value based on a condition
# x if condtion else y
# if condition iss true then return true otherwise return false 

num = int(input("Enter a number: "))
print("posative" if num>0 else "negative")# its print the posative bcz num is greater than 0
result = "EVEN"  if num%2>0 else "ODD"
print(result)