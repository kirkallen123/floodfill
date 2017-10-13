arr = [1, 2, [3, 4], 5, 6]
acc = 0

for i in arr:
    if type(i) == list:
        for x in i:
            acc += x
    else:
        acc += i

print(acc)
print(1 + 2 + 3 + 4 + 5 + 6)
