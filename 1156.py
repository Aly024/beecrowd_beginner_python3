elements = []

divisor = 1
power = 0

while (divisor < 40):

    dividend = 2**power
    S = divisor / dividend
    
    #print(f"{divisor}/{dividend}")

    elements.append(S)
    divisor += 2
    power += 1 
    

result = sum(elements)
print(f"{result:.2f}")
