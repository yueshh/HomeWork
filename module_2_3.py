my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
offCycle = True
index = 0
while offCycle:
    if my_list[index] < 0:
        offCycle = False
    if my_list[index] > 0:
        print(my_list[index])
    index += 1
