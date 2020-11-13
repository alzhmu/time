import time

k=0
for i in 1,10,100,1_000,10_000,100_000,1_000_000,10_000_000,100_000_000,1_000_000_000:
    a=range(i)
    for j in range(10):
        startTime = time.time()
        z=sum(a)
        endTime=time.time()
        print(i,endTime-startTime)