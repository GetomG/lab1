##working still havent done file
D1 = open(r"D:\WorkSpace\Python_Basic\lab_03\input\DESCRIBE_LOG_EVENTS_20230625_154002.txt",'r')
D2 = open(r"D:\WorkSpace\Python_Basic\lab_03\input\DESCRIBE_LOG_EVENTS_20230625_160416.txt",'r')
D3 = open(r"D:\WorkSpace\Python_Basic\lab_03\input\DESCRIBE_LOG_EVENTS_20230625_160558.txt",'r')



D1R = D1.read()

#Counting Active Line (Hardcode)

active_lst = []
count_active = 0


#Finding Total Active Lines
for lines in D1R.splitlines():
    #print(lines)
    if "active" in lines.split("|"):
        active_lst.append(lines)
        count_active += 1
   
print("Total active: ",count_active)


#Counting active and male
count_active_m = 0

for lines in D1R.splitlines():
    #print(lines)
    if "active" in lines.split("|") and "m" in lines.split("|"):
        count_active_m += 1
   
print("count_active_m: ",count_active_m)


#Counting active and female
count_active_f = 0

for lines in D1R.splitlines():
    #print(lines)
    if "active" in lines.split("|") and "f" in lines.split("|"):
        count_active_f += 1
   
print("count_active_f: ",count_active_f)


#Minimum & Maximum zip code
#Zip code at 3rd position
ziplst = []

for lines in D1R.splitlines()[1:]:
    field = lines.split("|")
    if len(field) > 3:
      zipcode = field[3]
      ziplst.append(zipcode)
       
print("min zip code is:", min(ziplst),"Max zip code is:",max(ziplst))


#Phone numbers???
#Extracting Phone numbers
phonelst = []
for lines in D1R.splitlines()[1:]:
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
with open('special_phonenumber.txt', 'w') as file:
    for item in phonenum_format:
        file.write(item + '\n')
#     print(no)

# for phonenum in phonenum_format:
#       if "x" in phonenum:
#          index = phonenum.index("x")
#          print(index)

    
