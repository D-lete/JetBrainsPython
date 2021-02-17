# put your python code here
def calculator():
    input_1 = float(input())
    input_2 = float(input())
    operator = input()
    if operator == '+':
        result = input_1 + input_2
        if operator == '-':
            result = input_1 - input_2
            if operator == '/':
                result = input_1 / input_2
                if operator == '*':
                    result = input_1 * input_2
                    if operator == 'mod':
                        result = input_1 % input_2
                        if operator == 'pow':
                            result = input_1 ** input_2
                            if operator == 'div':
                                result = input_1 // input_2

        print(result)
