number = []
for i in range(1,4):
    x = int(input(f"Введите число {i}: "))
    number.append(x)
ind1, ind2, ind3 = number[0], number[1], number[2]
if ind1 == ind2 == ind3:
    print('Вывод: 3')
elif ind1 == ind2 or ind3 == ind3 or ind2 == ind1:
    print('Вывод: 2')
else:
    print('Вывод: 0')
