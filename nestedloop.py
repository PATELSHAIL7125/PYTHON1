#nested loop = A loop inside a another loop (outer,innne)
                    #outer loop:
                    #inner loop:
row = int(input("Enter the number of rows: "))
column = int(input("Enter the number of columns: "))
symbol = input("Enter the symbol to be printed: ")
   
for x in range (row):
    print(end="\n")
    for y in range(column):
        print(symbol, end=" ")