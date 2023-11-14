N = int(input())

a = ( ( 1+(5)**0.5 ) / 2 ) ** N
b = ( ( 1-(5)**0.5 ) / 2 ) ** N

result = ( a-b ) / (5**0.5) 

print(f"{result:.1f}")