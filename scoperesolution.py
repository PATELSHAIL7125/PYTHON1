#variable scope = where a variable is visible and acessible 
#scope-resolution = (LEGB) Local, Enclosing, Global, Built-in

def func1():
    a=1; 
  #   print(b)  # func1 has no idea what b is 

def func2():
    b=2;
#    print(a)  # func2 has no idea what a is

func1()
func2()


#local version

# def func1():
#     x=1; 
#     print(x)  # func1 has no idea what b is 

# def func2():
#     x=2;
#     print(x)  # func2 has no idea what a is

# func1()
# func2()

# enclosed version 

def func1I():
    x=1;

    def func2():
    print(x)
    func2() 

func1()