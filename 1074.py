N = int(input())

string_1 =''
string_2 = ''

for i in range(N):

    val = int(input())

    if val == 0:
        print('NULL')

    else:

        if val % 2 == 0:
            string_1 = 'EVEN'
        else:
            string_1 = 'ODD'

        if val > 0:
            string_2 = 'POSITIVE'

        if val < 0:
            string_2 = 'NEGATIVE'

        print(f'{string_1} {string_2}')
