
from datetime import datetime
import os


DIRpath = "D:\WorkSpace\Python_Basic\lab_03\input"


#DESCRIBE_LOG_EVENTS_{YYYYMMDD}_{HHMMSS}.txt
#Date validation
correctfront = []
correctdate = []


print(os.path.isdir("D:\WorkSpace\Python_Basic\lab_03\input\DESCRIBE_LOG_EVENTS_20230625_160411.txt"))