#https://github.com/mzst00/beecrowd_py_mehedi

N1,N2,N3,N4 = list(map(float,input().split()))

avrg = ( (N1*2) + (N2*3) + (N3*4) + (N4*1) )/(2+3+4+1)

print("Media: %.1f"%avrg)

if avrg >=7:
    print('Aluno aprovado.')
elif avrg <5.0:
    print('Aluno reprovado.')
elif avrg >= 5.0 and avrg<6.9:
    print('Aluno em exame.')
    N5 = float(input())
    print('Nota do exame: %.1f'%N5)
    avrg5=(avrg+N5)/2
    if avrg5 >=5.0 :
        print('Aluno aprovado.')
    elif avrg5 <=4.9:
        print('Aluno reprovado.')
    print('Media final: %.1f'%avrg5)
