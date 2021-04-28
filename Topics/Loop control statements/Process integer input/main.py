# put your python code here
integers = []
integer = int(input())


def lister():
    for i in range(len(integers)):
        while 10 < integer < 100:
            integers.append(integer)
        print(integers)


lister()
