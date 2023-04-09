mode = input()
n = 12
matrix = []

for r in range(n):

    row = []

    for items in range(n):

        item = float(input())
        row.append(item)

    matrix.append(row)

no_of_items =  0
output = 0
mid = int(n/2)
for i in range(mid):

    item_select_top = matrix[i][n-i:]
    item_select_bottom = matrix[n-i-1][n-i:]

    no_of_items += ( len(item_select_top) + len(item_select_bottom) )
    output += ( sum(item_select_top) + sum(item_select_bottom) )

if mode == "S":

    print(f"{output:.1f}")

if mode == "M":

    output = output / no_of_items

    print(f"{output:.1f}")