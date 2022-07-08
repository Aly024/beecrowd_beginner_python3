'''
val = float(input())

lb = [0, 25, 50, 75]
ub = [25, 50, 75, 100]
lb_sign = '('
ub_sign = ']'

i = 0
while i in range(4):
    LB = lb[i]
    UB = ub[i]
    #print(i)

    if val < 0 or val > 100:
        print('Fora de intervalo')
        break

    elif LB <= val <= UB:
        if val == 25:
            lb_sign = '['
        print(f'Intervalo {lb_sign}{LB},{UB}{ub_sign}')
        break
        

    i += 1

'''

# Interval

a = float(input())

if a<0 or a>100 :
    print('Fora de intervalo')
elif a<=25:
    print('Intervalo [0,25]')
elif a<=50 :
    print('Intervalo (25,50]')
elif a<=75:
    print('Intervalo (50,75]')
else :
    print('Intervalo (75,100]')