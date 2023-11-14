#functions
def dash():
    dash_p = ""
    for i in range(39):
        dash_p += "-"
    print(dash_p)

def line(int_str, pos):
    list_p = []
    line_p = "|"
    for i in range(37):
        line_p += " "
    line_p += "|"
    list_p.append(line_p)
    o_str = "".join(list_p)
    #print(o_str)

    int_str_m1 = int_str[:len(o_str) - pos]
    #print(f"int_str_m1 = {int_str_m1}")
    o_str_m1 = o_str[:pos] + int_str_m1 + o_str[pos + len(int_str_m1):]
    print(o_str_m1)

#main program
dash()
line("x = 35", 1)
line("",1)
line("x = 35", 16)
line("",1)
line("x = 35", 32)
dash()