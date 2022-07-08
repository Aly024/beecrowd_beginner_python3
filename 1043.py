A,B,C = map(float,input().split())

if A+B>C and A+C>B and B+C>A:
    perimeter = A+B+C
    print(f'Perimetro = {perimeter}')

else:
    area_trapez = 0.5*(A+B)*C
    print(f'Area = {area_trapez}')
