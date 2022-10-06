#https://github.com/joy1954islam/uri-problem-solution-in-python/blob/master/problem%201175%20Array%20Change%20l.py
#https://www.w3schools.com/python/numpy/numpy_array_slicing.asp
a = []

for i in range(20):    
    N = int(input())
    a.append(N)


count = 0
for j in a[::-1]:
    print(f"N[{count}] = {j}")
    count += 1