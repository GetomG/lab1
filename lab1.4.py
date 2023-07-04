
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

for i in correcttime:
    print("ct",i)



#checking if it is not folder
newlst = []
D = 0
path = "D:\WorkSpace\Python_Basic\lab_03\input"
for filename in correcttime:
  combined_path = os.path.join(path, filename)
  if os.path.isdir(combined_path) == False:
        #print("Valid:",filename)
        newlst.append(combined_path)
        # D = open(combined_path)
        # DR = D.read(500)
        # print(DR)
        
print(newlst)

#################### End of Nightmare #######################


import logging

no_of_file_processed = 0
logging.basicConfig(level=logging.INFO, format='%(message)s')

for i in newlst:
    D = open(i)
    DR = D.read()

    record_count = 0
    for lines in DR.splitlines():
        record_count += 1

    # Log the record count
    logging.info("Number of records: %s", record_count)

    no_of_file_processed += 1

# Log the total number of files processed
logging.info("Total number of files processed: %s", no_of_file_processed)





for i in newlst:
    D = open(i)
    DR = D.read()

    active_lst = []
    count_active = 0
    #Finding Total Active Lines
    for lines in DR.splitlines():
        #print(lines)
        if "active" in lines.split("|"):
            active_lst.append(lines)
            count_active += 1
    
    print(f"Total {i} active: ",count_active)


    #Counting active and male
    count_active_m = 0

    for lines in DR.splitlines():
        #print(lines)
        if "active" in lines.split("|") and "m" in lines.split("|"):
            count_active_m += 1
    
    print("count_active_m: ",count_active_m)


    #Counting active and female
    count_active_f = 0

    for lines in DR.splitlines():
        #print(lines)
        if "active" in lines.split("|") and "f" in lines.split("|"):
            count_active_f += 1
    
    print("count_active_f: ",count_active_f)

                    
    #Minimum & Maximum zip code
    #Zip code at 3rd position
    ziplst = []

    for lines in DR.splitlines()[1:]:
        field = lines.split("|")
        if len(field) > 3:
            zipcode = field[3]
            ziplst.append(zipcode)
        
    print("min zip code is:", min(ziplst),"Max zip code is:",max(ziplst))


    
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
    phonenum_format = []

    for phonenum in phonelst:
        for char in phonenum:
            if char[0] == "(":
                #  index = char.index("x")
                #  print(index)
                if "x" in phonenum:
                    index = phonenum.index("x")
                    formatted = phonenum + ", x=" + phonenum[index+1:]
                    phonenum_format.append(formatted)
                else: 
                    phonenum_format.append(phonenum)
                #print("format",phonenum) 

    #Exporting
    with open('special_phonenumber2.txt', 'w') as file:
        for item in phonenum_format:
            file.write(item + '\n')








#       newlst.append(filename)

# print(newlst)



  
# print(combined_paths)

# print(datetime.strptime("2023 0625","%Y%m%d"))

# appended_list = []
# for item in correcttime:
#     appended_list.append(f"D:\WorkSpace\Python_Basic\lab_03\input\{item}")

# print(appended_list)



# filtered_files =[]
# # for file in os.listdir(DIRpath):
# #     for i in correcttime:
# #         if file == i:
# #             filtered_files.append(file)
# #             #x = os.open(DIRpath,file)

# for file in os.listdir(DIRpath):
#     if not os.path.isdir(file):
#         filtered_files.append(file)

# print(filtered_files)
