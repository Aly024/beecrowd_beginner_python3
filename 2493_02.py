while True:
    
    try:

        # Function to take input for expressions
        def input_expression(T):
            expressions = []
            for i in range(T):
                expression = input()
                expressions.append(expression)
            return expressions

        # Function to select the expression based on response
        def select_expression(expressions, response):
            selected_index = int(response.split()[1]) - 1  # Extract the index and adjust for 0-based indexing
            expression_selected = expressions[selected_index]
            operator_index = response.split()[2]
            return expression_selected, operator_index

        # Function to check the response
        def check_response(expression_selected, operator_index):
            actual_ans = expression_selected[-1]
            modified_expression = expression_selected.replace(" ", operator_index)
            verify_expression = modified_expression.split("=")
            verify_equation = eval(verify_expression[0])
            if verify_equation == int(actual_ans):
                return True
            else:
                return False

        # Main program
        T = int(input())

        expression_list = input_expression(T)
        response_list = []
        right = []
        wrong = []

        for i in range(T):
            response = input()
            response_list.append(response)

        for i, response in enumerate(response_list):
            expression_selected, operator_selected = select_expression(expression_list, response)
            if check_response(expression_selected, operator_selected):
                #print(f"Response {i+1}: Correct")
                right.append(response.split(" ")[0])
            else:
                #print(f"Response {i+1}: Incorrect")
                wrong.append(response.split(" ")[0])

        right.sort()
        wrong.sort()

        if len(wrong)<T:
            print(' '.join(wrong))
        elif len(right) == 0:
            print("None Shall Pass!")
        else:
            print("You Shall All Pass!")

    except EOFError:
        break