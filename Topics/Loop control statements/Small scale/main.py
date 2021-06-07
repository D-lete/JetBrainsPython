float_list = []
while float_list.__contains__(".") is False:
    buoys = input()
    float_list.append(buoys)
else:
    float_list.remove(("."))
    floated = [float(i) for i in float_list]
    print(min(floated))

