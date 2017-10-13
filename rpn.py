
input = "15 7 1 1 + - / 3 * 2 1 1 + + -"

#input = "3262123113 4231223313 +"

items = []
chars = input.split(' ')
ops = []

for x in chars:
    if x == "+" or x == "-" or x == "*" or x == "/":
        opperand2 = int(items.pop())
        opperand1 = int(items.pop())
        acc = 0
        if x == "+":
            acc = opperand1 + opperand2
        elif x == "-":
            acc = opperand1 - opperand2
        elif x == "*":
            acc = opperand1 * opperand2
        else:
            acc = opperand1 / opperand2
        ops.append(str(opperand1) + x + str(opperand2))
        items.append(acc)
    else:
        items.append(x)


print(items.pop())
print(ops)


