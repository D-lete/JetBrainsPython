message = list(input())
key = sum(int(input()).to_bytes(2, byteorder='little'))
print(''.join([chr((ord(x) + key)) for x in message]))
