# https://projecteuler.net/problem=9
import math

sqrs = []

for i in range(1, 1001):
    sqrs.append(i ** 2)

for i in sqrs:
    for y in sqrs:
        if i + y in sqrs:

            if math.sqrt(i) + math.sqrt(y) + math.sqrt(i + y) == 1000:
                print(int(math.sqrt(i) * math.sqrt(y) * math.sqrt(i + y)))
                break

