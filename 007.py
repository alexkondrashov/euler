import time

start_time = time.time()

def is_simple_num(n):
    for i in range(2, n + 1):
        if n % i == 0:
            if i == n:
                return True
            else:
                return False

i = 2
list_simple = []

while len(list_simple) < 10001:
    if is_simple_num(i):
        list_simple.append(i)
    i += 1

print('10001 - ', list_simple[10000])
print("--- %s seconds ---" % (time.time() - start_time))
