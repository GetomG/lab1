
from datetime import datetime
import os


DIRpath = "D:\WorkSpace\Python_Basic\lab_03\input"


#DESCRIBE_LOG_EVENTS_{YYYYMMDD}_{HHMMSS}.txt
#Date validation
correctfront = []
correctdate = []

    


for filename in os.listdir(DIRpath):
    items = filename.split("_")
    if ''.join(items[:3]) == "DESCRIBELOGEVENTS":
        correctfront.append(filename)

#Correct date format
for filename in correctfront:
    items = filename.split("_")
    #print(items)
    if len(items) > 3:
        #print(items[3])
        x = items[3]
        date_format = "%Y%m%d"
        try: 
            datetime.strptime(x,date_format)
            correctdate.append(filename)
        except:
            pass


correcttime = []

#correct time format
for filename in correctdate:
    items = filename.split("_")
    #print(items[4])
    if len(items) > 4:
        x = items[4].split(".")[0]
        try:
            time_format = "%H%M%S"
            datetime.strptime(x,time_format)
            correcttime.append(filename)
        except:
            pass

# for i in correcttime:
#     print("correctime",i)



#checking if it is not folder
newlst = []
D = 0
path = "D:\WorkSpace\Python_Basic\lab_03\input"
for filename in correcttime:
  combined_path = os.path.join(path, filename)
  if os.path.isdir(combined_path) == False:
        newlst.append(combined_path)
    
        
# print(newlst)

#################### End of Nightmare #######################


import logging

no_of_file_processed = 0
logging.basicConfig(level=logging.INFO, format='%(message)s')

for i in newlst:
    D = open(i)
    DR = D.read()

    record_count = 0
    for lines in DR.splitlines()[1:-1]:
        record_count += 1

    # Log the record count
    logging.info("Number of records in %s: [%s]", i, record_count)

    no_of_file_processed += 1

# Log the total number of files processed
print("\n")
logging.info("Total number of files processed: %s", no_of_file_processed)
print("----------------------")


accu_count_am = 0
accu_count_af = 0
phonenum_format = []
ziplst = []
last_file_index = len(newlst) - 1


## outside for loop, read through all the filtered files
for i in newlst:
    D = open(i)
    DR = D.read()

    #Finding Total Active
    active_lst = []
    count_active = 0
    #Finding Total Active Lines
    for lines in DR.splitlines():
        #print(lines)
        if "active" in lines.split("|"):
            active_lst.append(lines)
            count_active += 1
    
    print(f"File: \n {i} \n\nTotal active: ",count_active)

    #Exporting
    with open('active.txt', 'w') as file:
        for item in active_lst:
            file.write(item + '\n')


    #Counting active and male
    count_active_m = 0

    for lines in DR.splitlines():
        #print(lines)
        if "active" in lines.split("|") and "m" in lines.split("|"):
            count_active_m += 1
        
    accu_count_am += count_active_m
    print("count_active_m: ",count_active_m)
    


    #Counting active and female
    count_active_f = 0

    for lines in DR.splitlines():
        #print(lines)
        if "active" in lines.split("|") and "f" in lines.split("|"):
            count_active_f += 1

    accu_count_af += count_active_f
    
    print("count_active_f: ",count_active_f)

    print("----------------------")
    
    #print at last loop
    if i == newlst[-1]:
        print(f"total_count_am: [{accu_count_am}]")

    if i == newlst[-1]:
        print(f"total_count_af: [{accu_count_af}]")

    print("----------------------")


    #Minimum & Maximum zip code
    #Zip code at 3rd position

    for lines in DR.splitlines()[1:]:
        field = lines.split("|")
        if len(field) > 3:
            zipcode = field[3]
            ziplst.append(zipcode)

    if i == newlst[-1]:    
        print("min zip code is:", min(ziplst),"\nMax zip code is:",max(ziplst))

    print("----------------------")





    #Results Shown in another file
    #Phone numbers???
    #Extracting Phone numbers
    phonelst = []
    for lines in DR.splitlines()[1:]:
        field = lines.split("|")
        if len(field) > 10:
            phonenum = field[10]
            phonelst.append(phonenum)
    
    
    #Formatting
    #(xxx)(xxx-xxx)x=1234
    

    for phonenum in phonelst:
        for char in phonenum:
            if char[0] == "(":
                #  index = char.index("x")
                #  print(index)ca
                if "x" in phonenum:
                    index = phonenum.index("x")
                    formatted = phonenum.split("x")[0] + ", x=" + phonenum[index+1:]
                    phonenum_format.append(formatted)
                else: 
                    phonenum_format.append(phonenum)
                #print("format",phonenum) 



    #Exporting
    with open('special_phonenumber2.txt', 'w') as file:
        for item in phonenum_format:
            file.write(item + '\n')

#Print count
print(len(phonenum_format))