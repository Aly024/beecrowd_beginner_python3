while True:

    N = int(input())

    if N==0:
        break

    for r in range(1,N+1):
        z = 0
        y = 1
        for c in range(1,N+1):
            
            if r == 1:
                #print(f"  {c}",end=" ")
                print("%3d" %(c),end=" ")

            
            else:
                if (r-z)==0:
                    y+=1
                    #print(f"  {y}",end=" ")
                    print("%3d" %(y),end=" ")
                    
                else:
                    #print(f"  {r-z}",end=" ")
                    print("%3d" %(r-z),end=" ")
                    z+=1
                    
        print()
    print()  
