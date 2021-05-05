import statistics

count = int(input())
integers = []
for _ in range(count):
    integers.append(int(input()))
print(float(statistics.mean(integers)))
