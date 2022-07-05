'''
age = int(input())

year = age // 365
month = ( age % 365) // 30
day = ( age % 365) % 30
print('%d ano(s)' %year)
print('%d mes(es)' %month)
print('%d dia(s)' %day)

'''

age = int(input())

t = [365, 30, 1]
ans = []
text = ['ano(s)', 'mes(es)', 'dia(s)']

for i in t:
    quotient = int(age / i)
    ans.append(quotient)
    remainder = age % i
    age = remainder


for j in range(3):
    print(f'{ans[j]} {text[j]}')

