n = int(input())

values = [[0 for w in range(n)] for h in range(n)]

for a in range(n):
    val = input()  # takes in the string
    split = val.split(' ')
    values[a] = list(map(int, split))

# hold the totals:
# acc = [0 for h in range(n)]

print(values)
lakes = {}


def fill(x, y, vals, total, max):
    if vals[x][y] != 0:
        return total
    else:
        print("Looking at position: " + str(x) + "," + str(y))
        total += 1
        # vals[x][y] = -1 # set so we don't over recurse
        if x < max:
            # fill(x + 1, y, vals, total, max)
            if values[x + 1][y] == 0: total += 1
            if y < max:
                # fill(x + 1, y + 1, vals, total, max)
                if values[x + 1][y + 1] == 0: total += 1
            if y >= 0:
                # fill(x + 1, y - 1, vals, total, max)
                if values[x + 1][y - 1] == 0: total += 1
        if y < max:
            # fill(x, y + 1, vals, total, max)
            if values[x][y + 1] == 0: total += 1
        if y >= 0:
            # fill(x, y - 1, vals, total, max)
            if values[x][y - 1] == 0: total += 1
        if x >= 0:
            # fill(x - 1, y, vals, total, max)
            if values[x - 1][y] == 0: total += 1
            if y < max:
                # fill(x - 1, y + 1, vals, total, max)
                if values[x - 1][y + 1] == 0: total += 1
            if y >= 0:
                # fill(x - 1, y - 1, vals, total, max)
                if values[x - 1][y - 1] == 0: total += 1
    return total


for i in range(n):
    for j in range(n):
        if values[i][j] == 0:
            t = fill(i, j, values, 0, n - 1)
            print("Found at " + str(i) + str(j) + " = " + str(t))
            lakes[str(i) + str(j)] = t

tmp = lakes.values()
print(lakes)
print(tmp)
#