import moduleexam
pi = 3.14159

def square(x):
    return x ** 2;

def cube(x):
    return x ** 3;

def circumference(r):
    return 2 * pi * r;  

def area(r):
    return pi * r ** 2;

result = moduleexam.pi;
result1=moduleexam.area(5);
result2=moduleexam.circumference(5);
print(result);
print(result1);
print(result2);

