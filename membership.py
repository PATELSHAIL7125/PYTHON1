#MEMBERSHIP OPERATER =  USED TO WHETHER THE VALUE IOR VARIABLE IS FOUN D IN A SEQUENCE 
  #     (STRING,LIST,TUPLE,SET AND DICTIONARY)
#      1. IN
#      2. NOT IN 

word = "apple"

letter = input("guess the word")


if letter in word:
    print("yes")
else:
    print("no")

if letter not in word:
    print("yes")
else:
    print("no")

grades = {
    "John":90,
    "Jill":85,
    "Harry":70
}
student = input("Enter the student name")

if student in grades:
    print(f"{student} has scored {grades[student]}")
else:
    print("Student not found")


# for email 

email = "brocode@gmail.com" 

if "@" in email:
    print("email is valid")
else:
    print("email is invalid")