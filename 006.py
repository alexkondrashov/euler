# https://projecteuler.net/problem=6

def sum_sqr(num):
    res = 0
    for i in range(1, num + 1):
        res = res + i ** 2
    return res

def sqr_sum(num):
    res = 0
    for i in range(1, num + 1):
        res = res + i
    return res ** 2


if __name__ == "__main__":
    number = 100
    print(sqr_sum(number) - sum_sqr(number))
