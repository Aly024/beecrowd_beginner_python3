#functions

def func_eye(r,g,b):
    x = int(0.3*r + 0.59*g + 0.11*b)
    return x

def func_mean(r,g,b):
    rgb_list = [r,g,b]
    x = int(sum(rgb_list) / len(rgb_list))
    return x

def func_min_max(r,g,b, m_t):
    rgb_list = [r,g,b]
    x = None
    if m_t == "min":
        x = min(rgb_list)
    if m_t == "max":
        x = max(rgb_list)
    return x

#main program
T_C = int(input())

for i in range(T_C):

    method_type = input()
    R,G,B = map(int, input().split())
    result = 0

    if method_type == "eye":
        result = func_eye(R,G,B)

    if method_type == "mean":
        result = func_mean(R,G,B)

    if method_type == "min" or method_type == "max":
        result = func_min_max(R, G, B, method_type)
    
    print(f"Caso #{i+1}: {result}")
