# Function to take input for expresseion and response
def input_str(X, Y):

    for i in range(T):
        Y = input()
        X.append(Y)

# Function to select the expression based on response 
def select(X):
    selected_index = int(X.split()[1]) - 1  # Extract the index and adjust for 0-based indexing
    expression_selected = expression_list[selected_index]
    operator_index = (X.split()[2])
    return expression_selected, operator_index

def check(X, Y,index):
    actual_ans = expression_selected[-1]
    #print(f"Actual ans = {actual_ans}")
    modified_expression  = expression_selected.replace(" ",Y)
    verify_expression = modified_expression.split("=")
    verify_equ = eval(verify_expression[0])
    if verify_equ == int(actual_ans):
        #print(verify_equ)
        response_list = int(X.split())
        select_name = response_list
        #right.append(response_list)
        print(select_name)
    else:
        print("does not match")



T = int(input())

expression_list= []
response_list = []
right = []
wrong = []

expression_input_str = ""
response_input_str = ""

# Executing function for expresseion and response
input_str(expression_list, expression_input_str)
input_str(response_list,response_input_str)

#print(expression_list)
#print(response_list)

# For loop in serial number(sl_no)
for sl_no in response_list:

    # Executing func to select expression from response
    expression_selected, operator_selected = select(sl_no)
    #print(f"{expression_selected} {operator_selected}")
    check(expression_selected, operator_selected, sl_no)

