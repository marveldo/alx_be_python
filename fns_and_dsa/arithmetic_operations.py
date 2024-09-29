def perform_operation(num1,num2,operation):
    if operation == 'add':
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0 :
            raise ValueError('Cannot divde by zero')
        return num1/num2
    else:
        raise ValueError("Invalid Operation its only add, subtract, multiply, divide")