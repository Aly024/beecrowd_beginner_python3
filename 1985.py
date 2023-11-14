no_products = int(input())

products = {
    1001 : 1.5,
    1002 : 2.5,
    1003 : 3.5,
    1004 : 4.5,
    1005 : 5.5,
}
result = 0
for i in range(no_products):

    code , price = map(int,input().split(" "))
    
    for key,value in products.items():
        if code == key:
            result += value*price

print(f"{result:.2f}")