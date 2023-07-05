# Python program example to show the use of while loop   
  
num = 15  
  
# initializing summation and a counter for iteration  
summation = 0  
c = 1  
  
while c <= num: # specifying the condition of the loop  
    # begining the code block  
    summation = c**2 + summation  
    c = c + 1    # incrementing the counter  
  
# print the final sum  
print("The sum of squares is", summation)  





num = [34, 12, 54, 23, 75, 34, 11, 117, 876, 10045, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73]    
  
def prime_number(number):  
    condition = 0  
    iteration = 2  
    while iteration <= number / 2:  
        if number % iteration == 0:  
            condition = 1
            break  
        else:  
            iteration = iteration + 1  
  
    if condition == 0:  
        print(f"{number} is a PRIME number")  
    else:  
        print(f"{number} is not a PRIME number")  
for i in num:  
    prime_number(i)  




num = 21        
counter = 1      
# we will use a while loop for iterating 10 times for the multiplication table        
print("The Multiplication Table of: ", num)      
while counter <= 10: # specifying the condition  
    ans = num * counter      
    print (num, 'x', counter, '=', ans)      
    counter += 1 # expression to increment the counter  



# Python program to square every number of a list  
# initializing a list  
list_ = [3, 5, 1, 4, 6]  
squares = []  
# programing a while loop   
while list_: # until list is not empty this expression will give boolean True after that False  
    squares.append( (list_.pop())**2)  
# print the squares  
print( squares )  
