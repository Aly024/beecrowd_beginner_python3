#Taking 3 input as list
list = input().split(" ")

#Assigning values to a, b, c
a, b, c = list

#Calculating the greatest value using the given formula
#making string a, b, c to integer
ab = ( int(a) + int(b) + abs( int(a) - int(b) ) )/2
major_abc = ( int(ab) + int(c) + abs( int(ab) - int(c)) )/2

print("%d eh o maior" %major_abc)
