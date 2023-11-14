A, B, C = map(int, input().split())

result = ""


if (A-B) == 0 or (B-C) == 0 or (C-A) == 0:
    result = "S"

else:
    result = "N"

    binary_list = []
    for decimal_num in range(8):
        binary_num = bin(decimal_num)[2:].zfill(3)
        converted_num = [-1 if bit == '1' else 1 for bit in binary_num]
        binary_list.append(converted_num)

    #print(binary_list)

    for i in range(8):

        #print(f"i = {i}")
        #print(f"binary list = {binary_list[i]}")
        a = binary_list[i][0]
        b = binary_list[i][1]
        c = binary_list[i][2]

        A_ = A*a
        B_ = B*b
        C_ = C*c
        #print(f"A = {A_}")
        #print(f"B = {B_}")
        #print(f"C = {C_}")

        output = A_+B_+C_
        #print(f"output = {output}")

        if output == 0:
            result = "S"
            break
        else:
            result = "N"  

        #print(result)
        #print()
print(result)