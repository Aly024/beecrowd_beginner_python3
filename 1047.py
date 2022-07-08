#https://www.codeshikhi.com/2020/12/uri-1047-game-time-with-minutes-solution-in-c-cpp-cpluscplus-python.html

i_hr, i_min, f_hr, f_min = (map(int,input().split()))

diff_t = ((f_hr*60) + f_min) - ((i_hr*60) + i_min)

if diff_t <= 0:
    diff_t += 24*60

hour = diff_t // 60
minute = diff_t % 60

print(f'O JOGO DUROU {hour} HORA(S) E {minute} MINUTO(S)')