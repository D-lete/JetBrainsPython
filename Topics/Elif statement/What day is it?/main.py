def day_of_the_week():
    time_offset = int(input())
    current_time = 10.5
    if time_offset + current_time < 0:
        print('Monday')
    elif time_offset + current_time > 24:
        print('Wednesday')
    else:
        print('Tuesday')


day_of_the_week()
