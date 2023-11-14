a = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
b = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
c = ["","I","II","III","IV","V","VI","VII","VIII","IX"]

N = int(input())

latin = a[int(N/100)] + b[int((N%100)/10)] + c[N%10]

print(latin)