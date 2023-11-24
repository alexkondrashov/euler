import time

start_time = time.time()

exp = 2**1000
res_sum = 0

for i in range(0, len(str(exp))):
    res_sum = res_sum + int(str(exp)[i])

print(res_sum)
print("--- %s seconds ---" % int((time.time() - start_time)))
