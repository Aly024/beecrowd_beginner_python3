# In Python, you can calculate the quotient with // and the remainder with %.

'''
time = int(input())

hr = (time // 3600)
min = (time % 3600) // 60
sec = (time % 3600 ) % 60


print ("{}:{}:{}". format (hr,min,sec))

'''

val = int(input())

t = [3600, 60, 1]
ans = []

for i in t:
    quotient = int(val / i)
    ans.append(quotient)
    reminder = val % i
    val = reminder

print(f'{ans[0]}:{ans[1]}:{ans[2]}')