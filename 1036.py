#https://byjus.com/jee/quadratic-equations/

A,B,C = map(float, input().split())

D = (B*B)-(4*A*C)
if (A == 0) or (D < 0):

    print("Impossivel calcular") 

else: 

    r = ( (B*B)-(4*A*C) )**0.5

    x1 = (-B+r) / (2*A)
    x2 = (-B-r) / (2*A)

    print("R1 = %.5f" %x1)
    print("R2 = %.5f" %x2)