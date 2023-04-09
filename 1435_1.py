#Accepted
#https://www.youtube.com/watch?v=4PjIEClvDoY&ab_channel=Programa%C3%A7%C3%A3oLivre

while True:
    x = int(input())

    if(x == 0): 
        break

    #looping for row and columns
    for i in range(0, x):
        for j in range(0, x):
            
            #row
            if(i< x-i-1):
                distR = i
            else:
                distR = x-i-1

            #column
            if(j < x-j-1):
                distC = j
            else:
                distC = x-j-1

            #
            if(distC < distR):
                dist = distC
            else:
                dist = distR
            
            print("%3d" %(dist+1) , end="")
            
            if (j != x-1):
                print(end=" ")
        print()
    print()


    '''
    while True:

    N = int(input())

    if N == 0:
        break

    for i in range(N):
        for j in range(N):

            if i < N-1-i:
                R = i
            else:
                R = N-1-i

            if j < N-1-j:
                C = j
            else:
                C = N-1-j

            if C<R:
                val = C
            else:
                val = R

            print("%3d" %(val+1) , end="")
            #print(f"  {val+1}" , end="")

            if (j != N-1):
                print(end=" ")
        print()
    print()
    '''