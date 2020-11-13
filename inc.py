import time

k=0
for i in 1, 10, 100, 1_000, 10_000, 100_000, 1_000_000, 10_000_000, 100_000_000, 1_000_000_000:  # , 10_000_000_000
        startTime = time.time()
        for m in range(i):
            k+=1
        endTime=time.time()
        print(i,endTime-startTime)