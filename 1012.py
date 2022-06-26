# Taking input of 3 variables as list
list = input().split(" ")

A, B, C = list

TRIANGULO = 0.5 * float(A) * float(C)
CIRCULO = 3.14159 * (float(C))**2
TRAPEZIO = 0.5 * ( float(A) + float(B) ) * float(C)
QUADRADO = (float(B))**2
RETANGULO = float(A) * float(B)

print("TRIANGULO: %0.3f" %TRIANGULO)
print("CIRCULO: %0.3f" %CIRCULO)
print("TRAPEZIO: %0.3f" %TRAPEZIO)
print("QUADRADO: %0.3f" %QUADRADO)
print("RETANGULO: %0.3f" %RETANGULO)