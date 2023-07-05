D1 = open(r"D:\WorkSpace\Python_Basic\lab_03\input\DESCRIBE_LOG_EVENTS_20230625_154002.txt",'r')
D2 = open(r"D:\WorkSpace\Python_Basic\lab_03\input\DESCRIBE_LOG_EVENTS_20230625_160416.txt",'r')
D3 = open(r"D:\WorkSpace\Python_Basic\lab_03\input\DESCRIBE_LOG_EVENTS_20230625_160558.txt",'r')

D1R = D1.read()
#print(D1R)

# #1st Method of counting all records
# count = 0
# for lines in D1R.splitlines():
#     count += 1

# print("Total Records: ",count-2)

# def filter(find1,find2,D):

#     find_list = []

#     for lines in D.splitlines():
#       if find1 in lines and find2 in lines:
#          find_list.append(lines)
         
#     count = len(find_list)
#     return count

# print("a:", filter("|active|","a",D1R))     
# print("a_m: ",filter("|active|","|m",D1R))
# print("a_f: ",filter("|active|","|f",D1R))

active_lst = []
count_active = 0

for lines in D1R.splitlines():
    #print(lines)
    if "active" in lines.split("|"):
        active_lst.append(lines)
        count_active += 1
   
print(count_active)
#print(active_lst)

   # if "|active|" in lines:
   #    active_lst.append(lines)

#print(active_lst)

   # for line in lines:
   #    word = line.split("|")
   #    print(word)