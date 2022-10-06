'''
#https://github.com/joy1954islam/uri-problem-solution-in-python/blob/master/problem%201149%20Summing%20Consecutive%20Integers.py


#Take multiple inputs
lista = list(map(int, input().split()))


n1 = 'I'
n2 = 0
soma = 0

# For elements in list
#First iteration n1 = i
#keep looping until 
for i in lista:
    if (n1 == 'I'):
        n1 = i
        print(f"i = {n1}")
    else:
        if (i > 0):
            n2 = i
            print(f"n2 = {n2}")
            break
print("New loop")
for i in range(n2):
    soma += n1
    print(f"sum = {soma}")
    n1 += 1
    print(f"n1 = {n1}")

print(f"{soma}")

'''

sample = list(map(int, input().split()))

A = sample[0]
N = sample[-1]

total = [A]

for i in range(1,N):
    A += 1
    total.append(A)
    #print(A)

#print(total)
result = sum(total)
print(result)
