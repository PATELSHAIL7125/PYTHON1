# name = input("enter your full name:")

# result= len(name)
# print(result)
# #FIND METHOD    
# result1=name.find("a");
# print(result1)
# # capitalizee method 
# name1=name.capitalize()
# print(name1)
# #upper method 
# name2=name.upper()
# print(name2)
# #isdigit method 
# name3=name.isdigit()
# print(name3)
# #isalpha method
# name4=name.isalpha()
# print(name4)
# #count method 
# name5=name.count("a")
# print(name5)
# #replace method 
# name6=name.replace("a","e")
# print(name6)


#validate user input exercise 

#1. username is no more than 12 characters 
# 2. username must not conatin spaces 
# 3. username must not be conatain digits 

username = input("enter your username ")

if len(username)>12:
    print("USERNAME IS INVALID")
elif not username.find(" ") == -1:
    print("USERNAME IS INVALID")
elif username.isdigit():
    print("USERNAME IS INVALID")
else:
    print("USERNAME IS VALID")