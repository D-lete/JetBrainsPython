message = list(map(str, map(ord, input())))
print(''.join([str(chr(int(x) + 1)) for x in message]))
