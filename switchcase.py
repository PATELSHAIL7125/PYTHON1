# Match-case statement in Python 3.10
# an alternative to using many 'elif' statements 
# execute some code if a value mathes a 'case'
#Benifites: cleaner and syntax is more readable

def day_of_week(day):
    match day:
        case 1:
            print("Monday")
        case 2:
            print("Tuesday")
        case 3:
            print("Wednesday")
        case "thursday":  # case can be a string  or a number we also make like that 
              return True;
        case 5:
            print("Friday")
        case 6:
            print("Saturday")
        case 7:
            print("Sunday")
        case _:     # it is a wildcard stement like a default statement
            print("Invalid day")

day_of_week(3)

# Output:
# Wednesday