X,Y = map(int, input().split())

A = [ 0, 4.00, 4.50, 5.00, 2.00, 1.50]
 
sum = Y*(A[X])

print("Total: R$ %.2f" %sum)