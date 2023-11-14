while (True):
   
    try:
        u_m, u_d = map(int, input().split())

        month = [ 0, 1,2,3,4,5,6,7,8,9,10,11,12]
        days = [ 0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        #days remaining in current month
        d_r_c_m = days[u_m] - u_d
        #print(d_r_c_m)

        #days remaining in following month
        d_r_f_m = 0

        for i in range(u_m+1,13):
            #print(days[i])
            d_r_f_m += days[i]

        #print('days remaining in following month')
        #print(d_r_f_m)

        t_d_r = d_r_f_m + d_r_c_m
        t_d_r_f_CM= t_d_r-6

        if t_d_r_f_CM == 0:
            #print('Christmas') 
            print('E natal!') 

        elif t_d_r_f_CM == 1:
            #print('Christmas eve') 
            print('E vespera de natal!') 

        elif t_d_r_f_CM <= 359 and t_d_r_f_CM>0:
            #print('Total days remaining')
            #print(t_d_r_f_CM)
            print(f"Faltam {t_d_r_f_CM} dias para o natal!")

        else:
            #print('over') 
            print('Ja passou!') 

    except EOFError:
       break


