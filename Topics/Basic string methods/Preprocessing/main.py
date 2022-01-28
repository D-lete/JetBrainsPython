text = input()

t_0 = text.replace(",", "")
t_1 = t_0.replace(".", "")
t_2 = t_1.replace("!", "")
t_3 = t_2.replace("?", "")

print(t_3.lower())
