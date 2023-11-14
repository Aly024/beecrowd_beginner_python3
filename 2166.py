N = int(input())
b = 0
for i in range(N):

    b += 2
    b = 1/b

result = 1 + b
print(f"{result:.10f}")