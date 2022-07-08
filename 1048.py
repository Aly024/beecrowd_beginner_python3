#Reading the employee's salary
old_sal = float(input())

if 0<old_sal<=400.00:
    percentage = 15
if 400.01<=old_sal<=800.00:
    percentage = 12
if 800.01<=old_sal<=1200.00:
    percentage = 10
if 1200.01<=old_sal<=2000.00:
    percentage = 7
if old_sal>2000.00:
    percentage = 4

#Calculating new salary
new_sal = old_sal + (old_sal*(percentage/100))
print("Novo salario: %.2f" %new_sal)

#Calculating money earned
m_earned = new_sal - old_sal
print("Reajuste ganho: %.2f" %m_earned)

#printing the percentage
print("Em percentual:", percentage, "%")
