age = []

while True:

    N = int(input())
    if N < 0:
        break
    else:
        age.append(N)

average = sum(age) / len(age)
print(f"{average:.2f}")