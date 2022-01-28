prime = int(input())
flag = False
if prime > 1:
    for i in range(2, prime):
        if prime % i == 0:
            flag = True
            break
if flag or prime == 1:
    print('This number is not prime')
else:
    print('This number is prime')
