
# n → n/2 (n - четное)
# n → 3n + 1 (n - нечетное)

import time

start_time = time.time()

sequence_len = []
cnt = 0
n = 0

def get_next_num(num):
    if num % 2 == 0:
        return int(num / 2)
    else:
        return int(3 * num + 1)

for i in range(1, 1000001):
    n = i
    cnt = 0
    while n != 1:
        cnt += 1
        n = get_next_num(n)

    sequence_len.append(cnt + 1)

print('Макс длина последовательности ', max(sequence_len))
print('Начальный элемент с макс последоват', sequence_len.index(max(sequence_len)) + 1)
print("--- %s seconds ---" % int((time.time() - start_time)))