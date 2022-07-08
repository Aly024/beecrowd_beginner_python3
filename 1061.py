#https://www.codeshikhi.com/2021/08/uri-1061-event-time-solution-in-c-cpp-cplusplus-python.html

d1,s_d = input().split()
s_d = int(s_d)
s_hr, s_min, s_sec = map(int,input().split(":"))

d2,e_d = input().split()
e_d = int(e_d)
e_hr, e_min, e_sec = map(int,input().split(":"))

t_sec = e_sec - s_sec
t_min = e_min - s_min
t_hr = e_hr - s_hr
t_d = e_d - s_d

if t_sec < 0:
    t_sec += 60
    t_min -= 1

if t_min < 0:
    t_min += 60
    t_hr -= 1

if t_hr < 0:
    t_hr += 24
    t_d -= 1

print(f'{t_d} dia(s)')
print(f'{t_hr} hora(s)')
print(f'{t_min} minuto(s)')
print(f'{t_sec} segundo(s)')

'''
Dia 5
08 : 12 : 23
Dia 9
06 : 13 : 23
'''