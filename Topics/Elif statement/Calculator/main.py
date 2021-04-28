# put your python code here
def calculator():
    input_1 = float(input())
    input_2 = float(input())
    operator = input()
    if operator == '+':
        print(input_1 + input_2)
        if operator == '-':
            print(input_1 - input_2)
            if operator == '/' and input_2 == 0.0:
                print('Division by 0!')
                if operator == '/':
                    print(input_1 / input_2)
                    if operator == '*':
                        print(input_1 * input_2)
                        if operator == 'mod' and input_2 == 0.0:
                            print('Division by 0!')
                            if operator == 'mod':
                                print(input_1 % input_2)
                                if operator == 'pow':
                                    print(input_1 ** input_2)
                                    if operator == '//' and input_2 == 0.0:
                                        print('Division by 0!')
                                        if operator == '//':
                                            print(input_1 // input_2)
calculator()