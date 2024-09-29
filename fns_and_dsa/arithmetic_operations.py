

def perform_operation(num1 : float , num2 : float , operation : str):
    result = None
    match operation :
        case 'add' :
            result = num1 + num2
        case 'subtract' :
            result = num1 - num2
        case 'multiply' :
            result = num1 * num2
        case 'divide' :
            if num2 == 0 :
                raise ValueError('cannot divide by 0')
            else :
               result =  num1 / num2
    
    return result