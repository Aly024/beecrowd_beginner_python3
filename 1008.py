#Taking integer input of 
# employee's number, working hours, 
# amount per hour

NUMBER = int(input())
work_hour_month = int(input())
salary_hour = float(input())
SALARY =(( salary_hour )*( work_hour_month ))

print('NUMBER =',NUMBER)
print('SALARY = U$ %0.2f' %SALARY)