import random
 
# print(help(random))

random.randint(1,6) # it will generate a random number between 1 to 6
random.random() # it will generate a random number between 0 to 1
cards = ["ace","king","queen","jack"]
random.choice(cards)# method returns a random element from the non-empty sequence

random.shuffle(cards )# method shuffles the elements of a list in place
print(cards)

