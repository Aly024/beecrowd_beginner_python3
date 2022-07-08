#https://www.codeshikhi.com/2021/08/uri-1070-six-odd-numbers-solution-in-c-cpp-cplusplus-python.html

val = int(input())

i = 0

while (i<6):

    if(val%2 != 0):
        print(val)
        i += 1
    val += 1