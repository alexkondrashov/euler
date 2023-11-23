import time
from math import sqrt

start_time = time.time()
limit = 2000000
list_primes = []

def fill_prime():
    for i in range(2, limit + 1):
        for j in list_primes:
            if j > int((sqrt(i)) + 1):
                list_primes.append(i)
                break
            if i % j == 0:
                break
        else:
            list_primes.append(i)


fill_prime()
# print(list_primes)
print(sum(list_primes))

print("--- %s seconds ---" % round((time.time() - start_time), 2))

# 10K - 0.53 sec
# 100K - 38 sec
# 1 M ------

#        for j in list_primes:
# 10K - 0.05 sec
# 100K - 3.08 sec
# 1 M - 207 sec

#if j > int((sqrt(i)) + 1):
# 10K - 0.02 sec
# 100K - 0.29
# 1 M - 5.55