# https://projecteuler.net/problem=5


def calc():
    number = 20
    while True:
        for i in range(20, 0, -1):
            if number % i == 0:
                continue
            else:
                break

        if i == 1:
            break

        number += 20
    return number


if __name__ == "__main__":
    print(calc())





