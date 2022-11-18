import os

first ="import os\nimport time\nst= time.time()\n"
last ="tt = time.time() - st\nprint('time of execution of this code is : ', tt)"



atemp1=False
atemp2=False
while (atemp1==False):
    try:
        scriptone = input("\nfirst script : ")
        scriptf1 = open(f"{scriptone}.py", "r")
        atemp1=True
    except (FileNotFoundError):
        print("file not exist")
print("\n")
while (atemp2==False):    
    try:
        scripttwo = input("\nsocend script : ")
        scriptf2 = open(f"{scripttwo}.py", "r")
        atemp2=True
    except (FileNotFoundError):
        print("file not exist")
    
script1 = scriptf1.read()
script2 = scriptf2.read()

scriptf1.close
scriptf2.close

with open("log/test1.py", "w") as tester1:
    tester1.write(first)
    tester1.write(script1)
    tester1.write(last)
    tester1.write("\nwith open('log/values.txt', 'w') as val:\n")
    tester1.write("    val.write(str(tt))\n")
    tester1.write("val.close")

with open("log/test2.py", "w") as tester2:
    tester2.write(first)
    tester2.write(script2)
    tester2.write(last)
    tester2.write("\nwith open('log/values.txt', 'a+') as val:\n")
    tester2.write("    val.write(str(tt))\n")
    tester2.write("val.close")



tester1.close
tester2.close

os.system('python log/test1.py')
with open("log/values.txt", "a+") as f2:
    f2.write("\n")
f2.close
os.system('python log/test2.py')

values = open("log/values.txt", "r")
Lines = values.readlines()
values.close
#print(float(Lines[0]))
#print(float(Lines[1]))


if float(Lines[0])<float(Lines[1]):
    print(f"{scriptone} is better than {scripttwo}")
elif float(Lines[0])>float(Lines[1]):
    print(f"{scripttwo} is better than {scriptone}")





