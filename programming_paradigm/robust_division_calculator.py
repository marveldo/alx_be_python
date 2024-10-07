def safe_divide(numerator , denominator):
    try :
        numerator_value = float(numerator)
        denominator_value = float(denominator)
    except ValueError :
        return "Error: Please enter numeric values only."
    try :
        result = numerator_value/denominator_value
        return f'The result of the division is {result}'
    except ZeroDivisionError :
        return 'Error: Cannot divide by zero.'