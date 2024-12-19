#default arguments = A default value for certain parameters 
                    # default is used when that argument is omitted 
                    # make your function more flexible, reduce of arguments 
                    # 1.positional arguments
                    #2. default arguments   
                    #3. keyword arguments
                    # arbitrary arguments                    


import time;
def net_price(list_price,discount=0,tax=0.05): # IT IS A DEFAULT ARGUMENTS 
    return list_price * (1-discount) * (1+tax)


print(net_price(500)); # 500
print(net_price(500,0.10)); # 450
print(net_price(500,0,0.10))#550


def count(start,end):
    for x in range(start,end+1):
        print(x)
        time.sleep(1)

count(0,10)