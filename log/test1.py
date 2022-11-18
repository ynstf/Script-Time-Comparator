import os
import time
st= time.time()
i = 0
while(i<1000000):
    i+=1
    x=i**2
tt = time.time() - st
print('time of execution of this code is : ', tt)
with open('log/values.txt', 'w') as val:
    val.write(str(tt))
val.close
