# Creating Empty set  
set1 = set()  
  
set2 = {'James', 2, 3,'Python'}  
  
#Printing Set value  
print(set2)  
  
# Adding element to the set  
  
set2.add(10)  
print(set2)  
  
#Removing element from the set  
set2.remove(2)  
print(set2)  

import time
import random
import string
my_set = {4, 1, 7, 2, 5}  # Example set

print(my_set)

# add memmber is number ramdon
for i in range(0, 10) :
    # new_element = random.randint( 0, 512 )
    my_set.add(random.randint( 0, 512 ))

# add memmber is string ramdon
for i in range(0, 10) :
    letters = string.ascii_lowercase
    my_set.add(''.join(random.choice(letters) for i in range(10)))    
    print(my_set)

# display result    
print("member is {}".format(len(my_set)))
iCount = 0
while len(my_set) > 0 :
    iCount+=1
    print("member {} = {}".format(iCount,my_set.pop()))
    time.sleep(1)
