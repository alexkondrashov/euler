index = 1
fib = [1, 2]
limit = 4000000

while fib[index] + fib[index - 1] < limit:
    fib.append(fib[index] + fib[index - 1])
    index = index + 1

print(sum([fib[x] for x in range(0, len(fib)) if (fib[x] % 2) == 0]))