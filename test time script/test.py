import time
st= time.time()
for i in range(1000000):
    f=i**3
    c=f-i
tt = time.time() - st
print('time of execution of this code is : ', tt)
vr= input('press enter to leave')