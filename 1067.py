#https://www.codeshikhi.com/2021/08/uri-1067-odd-numbers-solution-in-c-cpp-cplusplus-python.html

val = int(input())

result = []

if val >=1 and val <= 1000:

    for i in range(val):

        if val %2 != 0:
            result.append(val)
        val -=1

result.sort()

for i in result:
    print(i)
        
'''

n = int(input())

for i in range(n+1):
    if(i%2==1):
        print(i)

'''