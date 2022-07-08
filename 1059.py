#https://stackoverflow.com/questions/47518609/for-loop-range-and-interval-how-to-include-last-step

def myrange(start,end,step):
    i = start
    while i < end:
        yield i 
        i += step
    yield end

for i in myrange(2,100,4):
    print(i)