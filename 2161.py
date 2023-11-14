N = int(input())
b = 0
for i in range(N):

    b += 6
    b = 1/b

result = 3 + b
print(f"{result:.10f}")