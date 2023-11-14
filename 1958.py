N = float(input())
sign = "+"
f = "{:.4e}".format(N)
if "-" in f[0:3]:
    sign = ""
f = f.upper()
print(f"{sign}{f}")