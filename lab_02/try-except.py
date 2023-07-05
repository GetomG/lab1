try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")


try:
    print(x)
except Exception as e:
    print("An exception occurred")

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

try:
    f = open("demofile2.txt","a")
    print("read file : demofile.txt done")
    try:
        f.write("\nLorum Ipsum")
        print("write sucsessful")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except:
    print("Something went wrong when opening the file")
