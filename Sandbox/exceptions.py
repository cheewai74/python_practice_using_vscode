
def print_sum(num1, num2):
    try:
        print(num1 + num2)
    except Exception:
        print("Could not add those numbers")
        
def print_multiply(num1, num2):
    if type(num1) != int or type(num2) != int:
        raise Exception('Inputs to the print_sum functions must be ints')
    print(num1 * num2)
        

try:    
    print_sum(1 ,'hi')
    print_sum(1,7)
except Exception as e:
    print(f'Something went wrong: {e}')

try:
    print_multiply(8,"space")
    print_multiply(8,8)
except Exception as e:
    print(f'Something went wrong: {e}')