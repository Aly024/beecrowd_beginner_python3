elements = []

for i in range(1,101):
    S = 1 / i
    elements.append(S)

result = sum(elements)
print(f"{result:.2f}")