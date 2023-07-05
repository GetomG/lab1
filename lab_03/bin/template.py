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
log.error("Test Error")
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

sys.exit(iRet) 
