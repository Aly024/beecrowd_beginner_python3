'''7 spaces
6 spaces b one space
5 space c 3 space 
4 space D five space 
3 space E seven space 
'''

space = " "

def a():
    print(f"{space*7}A")

def b():
    print(f"{space*6}B{space}B")

def c():
    print(f"{space*5}C{space*3}C")

def d():
    print(f"{space*4}D{space*5}D")

def e():
    print(f"{space*3}E{space*7}E")


#main
    
a()
b()
c()
d()
e()
d()
c()
b()
a()