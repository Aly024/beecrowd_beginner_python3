def blink_to_dec(r_c):

    final_r_c_l = []

    for item in r_c:

        if item == "-":
            final_r_c_l.append('0')
        if item == "*":
            final_r_c_l.append('1')

    final_r_c = ''.join(final_r_c_l)
    final_r_c = int(final_r_c,2)

    return final_r_c


result = []
while True:

    try:

        raw_code = input()

        if raw_code == "caw caw":
            lottery = sum(result)
            print(lottery)
            result = []

        else:
            converted_code = blink_to_dec(raw_code)
            result.append(converted_code)

    except EOFError:
        break