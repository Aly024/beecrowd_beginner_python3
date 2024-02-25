CPF = input()
row = []
for char in CPF:
    if(char == ".") or (char == "-"):
        continue
    else:
        row.append(char)

print("".join(row[:3]))
print("".join(row[3:6]))
print("".join(row[6:9]))
print("".join(row[-2:]))

