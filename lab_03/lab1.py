D1 = open(r"D:\WorkSpace\Python_Basic\lab_03\input\DESCRIBE_LOG_EVENTS_20230625_154002.txt",'r')
D2 = open(r"D:\WorkSpace\Python_Basic\lab_03\input\DESCRIBE_LOG_EVENTS_20230625_160416.txt",'r')
D3 = open(r"D:\WorkSpace\Python_Basic\lab_03\input\DESCRIBE_LOG_EVENTS_20230625_160558.txt",'r')

D1R = D1.read()
#print(D1R)

#1st Method of counting all records
count = 0
for lines in D1R.splitlines():
    count += 1

print("Total Records: ",count-2)

def filter(find1,find2,D):

    find_list = []

    for lines in D.splitlines():
      if find1 in lines and find2 in lines:
         find_list.append(lines)
         
    count = len(find_list)
    return count

print("a:", filter("|active|","a",D1R))     
print("a_m: ",filter("|active|","|m",D1R))
print("a_f: ",filter("|active|","|f",D1R))







#Filtering out only "active" status
active_lines = []
for lines in D1R.splitlines():
    if "|active|" in lines:
        active_lines.append(lines)

# #print(active_lines)

#counting active_lines
count_active = 0

for i in active_lines:
    count_active += 1

print ("Total active Records: ", count_active)


#counting Gender of active_lines
active_lines_m = []
for line in active_lines:
   if "|m" in line:
      active_lines_m.append(line)

count_active_m = 0

for i in active_lines_m:
    count_active_m += 1

print("count active m: ",count_active_m)

