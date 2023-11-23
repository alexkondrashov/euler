# https://projecteuler.net/problem=1
import time


def calc():
    res = sum([x for x in range(1, 1000) if ((x % 3) == 0) or ((x % 5) == 0)])
    return res


if __name__ == "__main__":
    start_time = time.time()
    print(calc())
    print("--- %s seconds ---" % (time.time() - start_time))
