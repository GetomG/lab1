# Declare a variable and initialize it  
x = 101  
  
# Global variable in function  
def mainFunction():  
    # printing a global variable  
    global x  
    print(x)  
    # modifying a global variable  
    x = 'Welcome To Javapoint'  
    print(x)  
  
mainFunction()
print(x)
