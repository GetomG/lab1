# Python program to demonstrate the application of iskeyword()  
# importing keyword library which has lists  
import keyword  
    
# displaying the complete list using "kwlist()."  
print("The set of keywords in this version is: Zai")  
print( keyword.kwlist )

for command in keyword.kwlist:
    print(command)