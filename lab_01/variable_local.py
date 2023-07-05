# Declaring a function  
def addingnumbers():  
    # Defining local variables. They has scope only within a function  
    a = 20  
    b = 30  
    c = a + b  
    print("The sum is:", c)  

    return c

e = addingnumbers()

#Calling a function  
addingnumbers()

# Accessing local variable outside the function   
print(e)  

#Ctrl shift K, deletes line
#hold alt to move line
#ctrl d to change name simultaneously