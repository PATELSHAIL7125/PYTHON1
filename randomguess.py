#  PYTHON GUESSING GAME 
import random

lowest_num=1;
highest_num=100;

random_num= random.randint(lowest_num,highest_num)
print("Welcome to the guessing game")

userinput = int(input(f"Enter a number between {lowest_num} and {highest_num}: "))
guesses =0 ;
is_running = True;
 
print(random_num) 
while is_running:
    guesses+=1
    if userinput == random_num:
        print(f"Congrats you have guessed the number in {guesses} guesses")
        is_running = False;
    elif userinput < random_num:
        print("Too low")
    else:
        print("Too high")
    userinput = int(input("Try again: "))

