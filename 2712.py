#https://github.com/mcavalca/uri-python/blob/master/2712.py

#by chat gpt
def has_number(s):
    for char in s:
        if char.isdigit():
            return True
    return False

n = int(input())
while n:
    n -= 1
    plate = input().split('-')
    
    if (len(plate) == 2) and (len(plate[0]) == 3) and (len(plate[1]) == 4) and (plate[0] == plate[0].upper() and (has_number(plate[0]) == False)):
        try:
            check = int(plate[1]) #Checking if 2nd part are all integer number
            r = int(plate[1][3]) #r = last digit of the second part
            if r > 8 or r == 0: # if last digit is 9 or 0
                print('FRIDAY')
            elif r > 6: # if last digit is 7 or 8
                print('THURSDAY')
            elif r > 4: # if last digit is 5 or 6
                print('WEDNESDAY')
            elif r > 2: # if last digit is 3 or 4
                print('TUESDAY')
            elif r > 0: # if last digit is 1 or 2
                print('MONDAY')
            else:
                print('FAILURE')
        except:
            print('FAILURE')
    else:
        print('FAILURE')