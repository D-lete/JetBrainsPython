# put your python code here
from statistics import mean

a, b = int(input()), int(input())
result_set = [i for i in range(a, b + 1) if i % 3 == 0]
print(float(mean(result_set)))
