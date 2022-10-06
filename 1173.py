N = int(input())

for i in range(10):
  X = 2**i             # this for loop is equivalent to N = [1,2,4,8,16,32,64, 128, 256, 512]
  output = N*X
  print(f"N[{i}] = {output}") 
  