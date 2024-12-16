#input() = A function that prompts the user to enter data 
#returns the entered data as string 

name = input("what is your name? ")

print(f"hello my name is a {name}")

age = int(input("what is your age? "))  

length = input("what is your length?");
width = input("what is youe width")
#area = length*width;#its give error bcz input is string so we have to convert it into a integer
area = int(length)*int(width)
print(f"the area is {area}cm")






