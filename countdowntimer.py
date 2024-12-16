import time # Import the time module

my_time = int(input("enter the time in seconds:"))

for x in range(my_time, 0, -1): # Loop from 10 to 0
    seconds = x%60;
    minutes = int(x/60)%60;
    hours = int(x/3600);
    print(f"{hours:02}:{minutes:02}:{seconds:02}") # Print the current value of x
    time.sleep(1)
 # Sleep for the time in seconds

print("Time's up!") # Print the message

