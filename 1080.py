result = {}

for i in range(100):
    N = int(input())
    result[i] = N

h_result_key = max(result, key=result.get)  
print(result[h_result_key])
print(int(h_result_key) + 1)




'''
#https://www.codeshikhi.com/2022/03/uri-bee-crowd-1080-highest-and-position-solution-in-c-cpp-python.html
j=0
loc=0
for i in range(100):
    n=int(input())
    if(n>j):
        j=n
        loc=i
print(j)
print(loc+1)
'''