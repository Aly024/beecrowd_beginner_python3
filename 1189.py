mode = input()
n = 12
matrix = []

for r in range(n):

    row = []

    for items in range(n):

        item = float(input())
        row.append(item)

    matrix.append(row)

#print(matrix)
output = 0
no_of_items = 0
mid = int(n/2)
for i in range(mid):

    item_select_top = matrix[i][:i]
    #print(f"top {item_select_top}")

    item_select_bottom = matrix[n-1-i][:i]
    #print(f" bottom {item_select_bottom}")

    no_of_items += ( len(item_select_top) + len(item_select_bottom) )
    output += ( sum(item_select_top) + sum(item_select_bottom))

if mode == "S":

    print(f"{output:.1f}")

if mode == "M":

    output = output / no_of_items
    print(f"{output:.1f}")