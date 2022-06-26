#Taking Radius of Sphere as input
R = float(input())

#Calculating volume of sphere
volume = (4/3) * 3.14159 * (R**3)  # R*R*R is equivalent to R**3
                                   # Python uses the ** operator for exponentiation,
                                   # not the ^ operator (which is a bitwise XOR):

print("VOLUME = %0.3f" %volume) 
