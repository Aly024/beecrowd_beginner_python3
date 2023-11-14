#while(True):

N = int(input())

upper_bound = [100, 85, 60, 35]
lower_bound = [86, 61, 36, 1]
grade = ["A", "B", "C", "D"]

if N == 0:
    print("E")

else:
    for i in range(4):
        u = upper_bound[i]
        l = lower_bound[i]
        if l <= N <= u:
            print(grade[i])