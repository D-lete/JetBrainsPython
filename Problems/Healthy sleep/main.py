def sleep():
    min_sleep = int(input())
    max_sleep = int(input())
    actual = int(input())
    if max_sleep >= actual >= min_sleep:
        print('Normal')
    elif actual > max_sleep:
        print('Excess')
    else:
        print('Deficiency')


sleep()
