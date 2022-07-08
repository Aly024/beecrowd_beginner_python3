#https://www.codeshikhi.com/2021/08/uri-1071-sum-of-consecutive-odd-numbers-i-solution-in-c-cpp-cplusplus-python.html

X = int(input())
Y = int(input())
start = min(X,Y)+1
end = max(X,Y)
if start % 2 == 0:
    start += 1

sum = 0
for i in range(start, end, 2):
    sum += i
print(sum)