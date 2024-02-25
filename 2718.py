#functions

def consecutive(X):

    #convert string to list
    bin_str = list(X)
    #print(fbin_str = bin_str}")

    #counting the consecutive number of "1"
    #If there is 0 counting resets
    highest_count_list = []
    count = 0

    for i in range(len(bin_str)):

        X = bin_str[i]

        if X == "1":
            count += 1

        elif X == "0":
            highest_count_list.append(count)
            count = 0
        
        if i == len(bin_str) - 1:
            highest_count_list.append(count)

    highest_count_list.sort(reverse = True)
    highest_count = highest_count_list[0]
    #print(f"highest_counts_recorded = {highest_count}")

    return highest_count


#Main program
N = int(input())

for i in range(N):

    dec_val = int(input())
    bin_val = bin(dec_val)[2:]
    #print(f"bin_val = {bin_val}")
    #print(f"bin_val_type = {type(bin_val)}")

    answer = consecutive(bin_val)
    print(answer)