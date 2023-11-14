old, new = map(float, input().split(" "))

increase = new - old
per_increase = (increase / old) *100

print(f"{per_increase:.2f}%")