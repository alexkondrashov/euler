
table = [[0 for _ in range(25)] for _ in range(25)]

res = 0

with open('11.txt', 'r') as file:
    lines = file.readlines()

for i in range(20):
    for j in range(20):
        table[i][j] = int(lines[i][j * 3: j * 3 + 2])


for i in range(20):
    for j in range(20):
        pass


print(res)
