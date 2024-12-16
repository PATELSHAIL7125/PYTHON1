#for loop - execute a block of code a fixed number of times 
     # you can iterate over a range,strings,sequence 

for xi in range(1,11):
    print(xi)


#reversed function 

for x in reversed(range(1,11)):
     print(x)  

#we also add step in for loop 

for x in range(1,11,2):
     print(x)

credit_number= "1234-5678-3456" ;


print("crdeit number is: ",credit_number)

for x in credit_number:
     print(x)


#if we continue to one element to another element
 
print("continue statement") 
for x in range(1,11):
   if x==5:
     continue
   else:
     print(x)