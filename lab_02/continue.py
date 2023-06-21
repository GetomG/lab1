# Python code to show example of continue statement  
   
# looping from 10 to 20  
for iterator in range(10, 21):  
   
    # If iterator is equals to 15, loop will continue to the next iteration  
    if iterator == 15:  
        continue  
    # otherwise printing the value of iterator  
    print( iterator )  



# Creating a string  
string = "JavaTpoint"  
# initializing an iterator  
iterator = 0  
   
# starting a while loop                   
while iterator < len(string):  
    # if loop is at letter a it will skip the remaining code and go to next iteration  
    if string[iterator] == 'a':    
        continue    
    # otherwise it will print the letter  
    print(string[ iterator ])  
    iterator += 1      