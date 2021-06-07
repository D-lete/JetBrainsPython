challenge = int(input())
if challenge in squares.keys():
    print(squares.pop(challenge))
    print(squares)
else:
    print('There is no such key')
    print(squares)
