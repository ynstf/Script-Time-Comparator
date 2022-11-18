import os

first ="import time\nst= time.time()\n"
last ="tt = time.time() - st\nprint('time of execution of this code is : ', tt)"


script = input("script : ")

scriptf = open(f"{script}.py", "r")

script = scriptf.read()

scriptf.close  

with open("test.py", "w") as tester:
    tester.write(first)
    tester.write(script)
    tester.write(last)
    tester.write("\nvr= input('press enter to leave')")
  
tester.close

os.system('python "test.py')
