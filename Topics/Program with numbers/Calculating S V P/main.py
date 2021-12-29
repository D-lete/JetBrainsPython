# put your python code here
input_l = int(input())
input_w = int(input())
input_h = int(input())

edges = 4 * (input_l + input_w + input_h)
surface = 2 * ((input_l * input_w) + (input_w * input_h) + (input_l * input_h))
volume = input_l * input_w * input_h

print(edges)
print(surface)
print(volume)