# *args = allows to pass multiple non- key arguments 
# **kwargs = allows to pass multiple key arguments
         #  *unpacking operator

def add(*args):  # *args = allows to pass multiple non- key arguments
    for arg in args: # args is a tuple
        total=0;
        total+=arg;
    return total

print(add(1,2,3))


def  print_kwargs(**kwargs): # **kwargs = allows to pass multiple key arguments
    #print(kwargs)# kwargs is a dictionary
    for i in kwargs.values():
        print(i)


print_kwargs(name="John",age=25,city="New York")


# BOTH USE OF ARGS AND KWARGS

def shipping_lable(*args,**kwargs):
    print(args)
    print(kwargs)

shipping_lable("Dr","Spongebob","Squarepants",
               country="USA",
               city="shinigan",
               zip="12345")