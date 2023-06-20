
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
        if val <= 25:    # It was if val == 25: previously. Thanx to Yasin Hayat Khan for solving it. Student of IIUC EEE Dept.
            lb_sign = '['
        print(f'Intervalo {lb_sign}{LB},{UB}{ub_sign}')
        break
        

    i += 1


