#format specifier = {:flags} formate a value based on what flags are intreseted

# .(number) = round to that many decimal places(fixed point notation)
# :(number) = allocate that many spaces 
# :03 = allocate and zero pad that many spaces
# :< left justify 
# :> right justify
# :^ center align
# :+ = use a plus sign to indiacte posative value 
# :- = place a sign to left most position 
# := = place a sign to left most position
# :  = insert a space before the posative numbers 
# :, = comma opeator 
 
price1 = 3.14159
price2  = -98700.65
price3 = 12.34

print(f"price1: {price1: .2f}");
print(f"price2: {price2:2f}");
print(f"price3: {price3:.2f}");

print(f"price1: {price1: 10}") 
print(f"price1:{price1:010}")#0003.14159
print(f"price1:{price1:<10}")#its mean left shift 
print(f"price1:{price1:^10}")#its mean center align 
print(f"price1:{price1:+}")#+3.14159
print(f"price2 :{price2:,}")

#we use many format specifer at a same time 

print(f"price2:{price2:,.2f}")