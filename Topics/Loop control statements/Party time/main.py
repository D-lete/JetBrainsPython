guest_list = []
while 1 == 1:
    guest = input()
    guest_list.append(guest)
    if "." in guest_list:
        guest_list.remove(".")
        print(guest_list)
        print(int(len(guest_list)))
        break
