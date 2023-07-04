import os
import glob
import configparser
import sys, getopt

import time

import re

import pandas as pd
import logging
import logging.handlers

import __main__

#----------------------------------------- Variable ------------------------------------------
EXEC_PARA  ='N/A'
EXEC_PARA='-f <Config file>'
conn = None
iRet = 0

#----------------------------------------- Logging ------------------------------------------
logFormatter = logging.Formatter('[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s')
logging.basicConfig(stream=sys.stdout, format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s')

log = logging.getLogger()
# log.setLevel(logging.DEBUG)
log.setLevel(logging.INFO)


#----------------------------------------- Function ------------------------------------------



#------------------------------------------ Argment ------------------------------------------
# try:
#     opts, args = getopt.getopt(sys.argv[1:],"hvf:t:d:",["conf=","type=","test"])
# except getopt.GetoptError:
#     # log.info('usage: {} -f <config file>'.format(sys.argv[0]))
#     _usage(sys.argv)
#     sys.exit(2)

# # set initiai value
# CONF = "N/A"
# FILE_TYPE = "N/A"
# DB_TYPE = "N/A"
MODE = "N/A"

# INPUT_PATH     = "N/A"
# INPUT_FILENAME = "N/A"

# for opt, arg in opts:
#     # log.info(opt)
#     if opt == '-h':
#         # log.info('usage: {} -f <config file>'.format(sys.argv[0]))
#         _usage(sys.argv)
#         sys.exit(2)
#     elif opt in ("-f", "--conf"):
#         CONF = arg
#     elif opt in ("-t", "--type"):
#         FILE_TYPE = arg
#     elif opt in ("-d", "--database"):
#         DB_TYPE = arg        
#     elif opt in ("-v","--test"):
#         MODE = "Unit Test"        
#     else:
#         _usage(sys.argv)

# if len(sys.argv) <= 1 :
#     _usage(sys.argv)




#------------------------------------------- Main --------------------------------------------
# log.info("__name__ : {}".format(__name__))

if __name__ == "__main__" and MODE == "Unit Test":
    log.info("Start Unit Test")
    import doctest

log.info("Hello World : {}".format(__name__))

with open(r"lab_03/input/DESCRIBE_LOG_EVENTS_2021_01_24_20210725_170200.csv",'r') as fs :

    # It will read the 4 characters from the text file  
    con = fs.read(4)
    # print(con) 

    # It will read the 10 characters from the text file  
    con1 = fs.read(10) 
    # print(con1) 

    # It will read the entire file 
    con2 = fs.read()
    # print(con2) 

    # for line in con2:
    #     print(line)
    #     time.sleep(5)

    for line in fs:
        print(line)
        time.sleep(5)
    
    fs.seek(0)
    con3 = fs.readlines()
    for line in con3:
        
        # remove last charecter
        line = line[:-1]

        print(line)
        time.sleep(5)
        

# read file by while loop
myfile = open(r"lab_03/input/DESCRIBE_LOG_EVENTS_2021_01_24_20210725_170200.csv",'r')

while myfile:
    line  = myfile.readline()
    print(line)
    time.sleep(5)

    if line == "":
        break
myfile.close() 

sys.exit(iRet)
