#taking input of 
# Seller's Name, salary 
# and sale's

name = input()
salary = float(input())
sales = float(input())

#Calculating the total income 
total = salary + (0.15*sales)


print('TOTAL = R$ %0.2f' %total)

