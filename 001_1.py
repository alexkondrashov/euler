# https://projecteuler.net/problem=1
import time


def calc():
    res = 0
    for i in range(1, 1000):
        if i % 3 == 0 or i % 5 == 0:
            res += i
    return res


if __name__ == "__main__":
    start_time = time.time()
    print(calc())
    print("--- %s seconds ---" % (time.time() - start_time))
