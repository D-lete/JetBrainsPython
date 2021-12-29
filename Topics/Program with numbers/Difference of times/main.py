# put your python code here
time_hours_one = int(input())
time_minutes_one = int(input())
time_seconds_one = int(input())

time_one = (time_hours_one * 3600) + (time_minutes_one * 60) + time_seconds_one

time_hours_two = int(input())
time_minutes_two = int(input())
time_seconds_two = int(input())

time_two = (time_hours_two * 3600) + (time_minutes_two * 60) + time_seconds_two

output = (time_two - time_one)
print(output)