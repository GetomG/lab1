# -----------------------------------------------------------------------------
# Section 1
# -----------------------------------------------------------------------------
# Code to find the sum of squares of each element of the list using for loop  
  
# creating the list of numbers  
numbers = [3, 5, 23, 6, 5, 1, 2, 9, 8]  
  
# initializing a variable that will store the sum  
sum_ = 0  
  
# using for loop to iterate over the list  
for num in numbers:  
     
sum_ = sum_ + num ** 2   
  
print("The sum of squares is: ", sum_)

# -----------------------------------------------------------------------------
# Section 2
# -----------------------------------------------------------------------------

# range
my_list = [3, 5, 6, 8, 4]  
for iter_var in range( len( my_list ) ):  
    my_list.append(my_list[iter_var] + 2)  
    print( my_list )




# -----------------------------------------------------------------------------
# Section 3
# -----------------------------------------------------------------------------
# code to print marks of a student from the record  
student_name_1 = 'Itika'  
student_name_2 = 'Parker'  
  
  
# Creating a dictionary of records of the students  
records = {'Itika': 90, 'Arshia': 92, 'Peter': 46}  

def marks( student_name ):  
    
    for a_student in record: # for loop will iterate over the keys of the dictionary  
        if a_student == student_name:  
            return records[ a_student ]  
            break  
    else:  
        return f'There is no student of name {student_name} in the records'   
          
# giving the function marks() name of two students  
print( f"Marks of {student_name_1} are: ", marks( student_name_1 ) )  
print( f"Marks of {student_name_2} are: ", marks( student_name_2 ) )  


# -----------------------------------------------------------------------------
# Section 4
# -----------------------------------------------------------------------------

# Nested Loops
import random  
numbers = [ ]  
for val in range(0, 11):  
    numbers.append( random.randint( 0, 11 ) )  
for num in range( 0, 11 ):  
    for i in numbers:  
        if num == i:  
            print( num, end = " " ) 

# Python program to show how to use continue loop control  
  
# Initiating the loop  
for string in "While Loops":  
    if string == "o" or string == "i" or string == "e":  
         continue  
    print('Current Letter:', string)  
    