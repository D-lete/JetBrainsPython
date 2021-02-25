n = int(input())

for i in range(n):
    value = int(input())
    if value % n == 0:
        print(value ** 2)
