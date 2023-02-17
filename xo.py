print('''Добро пожаловать в игру "Крестики-нолики"!\n
Игра имеет несколько простых правил:
1. Чтобы победить, вам нужно выстроить в ряд "x" или "0";
2. Игра имеет ограниченное число ходов;
3. Если вы промахнётесь, вы пропустите свой ход;
4. "x" ходят первыми.\n
Вот ваше стартовое поле:''')

str_1 = ['\\','1','2','3']
str_2 = ['1','-','-','-']
str_3 = ['2','-','-','-']
str_4 = ['3','-','-','-']

str_all = [' '.join(str_1), ' '.join(str_2), ' '.join(str_3), ' '.join(str_4)]
print('\n'.join(map(str, str_all)))

def shag(shag_g, shag_v, shag_z):
    if shag_g == 1:
        if str_2[shag_v] == '-':
            str_2[shag_v] = shag_z
            str_all = [' '.join(str_1), ' '.join(str_2), ' '.join(str_3), ' '.join(str_4)]
            print('\n'.join(map(str, str_all)))
        else:
            print("Клетка уже занята! За невнимательность вы пропускаете ход!")
    elif shag_g == 2:
        if str_3[shag_v] == '-':
            str_3[shag_v] = shag_z
            str_all = [' '.join(str_1), ' '.join(str_2), ' '.join(str_3), ' '.join(str_4)]
            print('\n'.join(map(str, str_all)))
        else:
            print("Клетка уже занята! За невнимательность вы пропускаете ход!")
    elif shag_g == 3:
        if str_4[shag_v] == '-':
            str_4[shag_v] = shag_z
            str_all = [' '.join(str_1), ' '.join(str_2), ' '.join(str_3), ' '.join(str_4)]
            print('\n'.join(map(str, str_all)))
        else:
            print("Клетка уже занята! За невнимательность вы пропускаете ход!")
    else:
        print("Вы ввели неправильное значение! За невнимательность пропускаете ход!")

def pruf(shag_z):
    usl1 = str_2[1] == str_2[2] == str_2[3] == shag_z
    usl2 = str_3[1] == str_3[2] == str_3[3] == shag_z
    usl3 = str_4[1] == str_4[2] == str_4[3] == shag_z
    usl4 = str_2[1] == str_3[1] == str_4[1] == shag_z
    usl5 = str_2[2] == str_3[2] == str_4[2] == shag_z
    usl6 = str_2[3] == str_3[3] == str_4[3] == shag_z
    usl7 = str_2[1] == str_3[2] == str_4[3] == shag_z
    usl8 = str_2[3] == str_3[2] == str_4[1] == shag_z
    usl0 = [usl1, usl2, usl3, usl4, usl5, usl6, usl7, usl8]
    res = any(usl0)
    return res

for i in range(1,6):
    if not i == 5:
        shag_z = 'x'
        shag_g = input("Введите значение для " + shag_z + " по горизонтали: ")
        shag_v = input("Введите значение для " + shag_z + " по вертикали: ")
        shag(int(shag_g), int(shag_v), shag_z)
        if pruf(shag_z):
            print("Есть ряд! Победили: " + shag_z)
            break

        shag_z = '0'
        shag_g = input("Введите значение для " + shag_z + " по горизонтали: ")
        shag_v = input("Введите значение для " + shag_z + " по вертикали: ")
        shag(int(shag_g), int(shag_v), shag_z)
        if pruf(shag_z):
            print("Есть ряд! Победили: " + shag_z)
            break

        i += 1
    else:
        shag_z = 'x'
        shag_g = input("Введите значение для " + shag_z + " по горизонтали: ")
        shag_v = input("Введите значение для " + shag_z + " по вертикали: ")
        shag(int(shag_g), int(shag_v), shag_z)

        print("Игра окончена! Ходов больше нет!")

        if pruf('x'):
            print("Победили x!")
        elif pruf('0'):
            print("Победили 0!")
        else:
            print("Ничья!")
        break