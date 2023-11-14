C_a, B_a, P_a = map(int, input().split())
C_r, B_r, P_r = map(int, input().split())
result = 0
#requested - available
if C_r > C_a:
    d_c = C_r - C_a
    result += d_c
if B_r > B_a:
    d_b = B_r - B_a
    result += d_b
if P_r > P_a:
    d_p = P_r - P_a
    result += d_p

print(result)