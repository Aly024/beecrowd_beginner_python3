#functions
def dash():
    dash_p = ""
    for i in range(39):
        dash_p += "-"
    print(dash_p)

def line():
    for i in range(5):       
        line_p = "|"
        for i in range(37):
            line_p += " "
        line_p += "|"
        print(line_p)


#main program
dash()
line()
dash()