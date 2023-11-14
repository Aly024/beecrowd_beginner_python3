import math

N = int(input())

P = N / math.log(N, 2.718281828)
M = 1.25506*P

print(f"{P:.1f} {M:.1f}")