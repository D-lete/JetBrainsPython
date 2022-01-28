score = int(input())
total = int(input())

if .90 <= score / total:
    print('A')
elif .8999 >= score / total >= .80:
    print('B')
elif .7999 >= score / total >= .70:
    print('C')
elif .6999 >= score / total >= .60:
    print('D')
elif .60 > score / total:
    print('F')
