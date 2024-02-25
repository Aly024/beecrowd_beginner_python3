#no. of employee in each floor
A_1 = int(input())
A_2 = int(input())
A_3 = int(input()) 

time_taken_list = []

t_1st_floor = A_2*2 + A_3*4
t_2nd_floor = A_1*2 + A_3*2
t_3rd_floor = A_1*4 + A_2*2

time_taken_list.append(t_1st_floor)
time_taken_list.append(t_2nd_floor)
time_taken_list.append(t_3rd_floor)

time_taken_list.sort()
print(time_taken_list[0])
