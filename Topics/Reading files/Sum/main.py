file = open('sums.txt', 'r')
while file.readline()[0:] != '':
    line = file.readline().split()
    print(int(line[0]) + int(line[1]))
file.close()
