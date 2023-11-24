
numbers = []

with open('013.txt', 'r') as file:
    lines = file.readlines()

for i in range(0, 100):
    numbers.append(int(lines[i]))

print('sum is ', sum(numbers))
print('result is ', str(sum(numbers))[0:10])
