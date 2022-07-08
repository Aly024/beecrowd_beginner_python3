start_time,end_time = map(int, input().split())
 
if start_time > end_time:
    duration = 24 - (start_time - end_time)
    print("O JOGO DUROU %d HORA(S)" %duration )

elif end_time > start_time:
    duration = end_time - start_time
    print("O JOGO DUROU %d HORA(S)" %duration ) 

elif start_time == end_time:
    
    print("O JOGO DUROU 24 HORA(S)" )


 