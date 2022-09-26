#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i == j:
            continue
        elif i > j:
            continue
        elif i == 8 and j == 9:
            continue
        else:
            print('{}{}, '.format(i, j), end="")
print(89)
