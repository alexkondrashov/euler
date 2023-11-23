import time

num = 600851475143
start_time = time.time()
diveders = []

# Finding all dividers of num
for i in range(2, num):
    if num % i == 0:
        if i in diveders:
            break
        diveders.append(i)
        diveders.append(int(num / i))

diveders.sort(reverse=True)

# Is number a simple num
def is_simple_num(n):
    for i in range(2, n + 1):
        if n % i == 0:
            if i == n:
                return True
            else:
                return False

# Finding result
for i in diveders:
    if is_simple_num(i):
        print("The largest prime factor of the number 600851475143 is %i " % i)
        break

print("--- %s seconds ---" % (time.time() - start_time))
