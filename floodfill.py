
n = int(input("Enter size of array dimensions in N (X * Y):"))

values = [[0 for w in range(n)] for h in range(n)]

for a in range(n):
    val = input("Enter in "+n+" numbers (0,1 or 2) space delimited:")
    split = val.split(' ')
    values[a] = list(map(int, split))

# pad the array so we don't have to check for edges in the recursive function:
real_values = [[-1 for width in range(n + 2)] for height in range(n + 2)]

#fill array inside the edges with the correct values input via stdin
for row in range(n):
    for col in range(n):
        real_values[row+1][col+1] = values[row][col]


def find_lake_body(c_row, c_col, map, total):
    if map[c_row][c_col] == -1:
        #found edge, send total back
        return total
    else:
        if map[c_row][c_col] == 0:
            total += 1
            #we've found this lake area, but it's not a edge, so lets set it to some magic value so we don't calculate
            #it again
            map[c_row][c_col] = -2
            #possible positions for current checked point:
            #down, right, up, left, up-right, up-right, down-left, down-right, up-left
            arr = [[1, 0], [0, 1], [-1, 0], [0, -1], [-1, 1], [1, -1], [1, 1], [1, -1]]
            for (x, y) in arr:
                total = find_lake_body(c_row + x, c_col + y, map, total)
            return total
        else:
            return total


lakes = {}

# find the lakes:
for i in range(n):
    for j in range(n):
        if values[i][j] == 0:
            lakes[(i, j)] = find_lake_body(i + 1, j + 1, real_values, 0)

final = list(lakes.values())
final.sort()

# we may have found some lakes that have already been found, in this case we have some 0's
# filter out the 0's
for n in final:
    if n > 0:
        print(n)
