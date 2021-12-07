from random import*
from keyboard import* 
igra = ["ножницы","бумага","камень"]
results1 =[]
results2 =[]
print("************************** Добро пожаловать в игру! **************************")
while 1: 
    try:
        vibor=int(input("Будете играть с человеком или ботом. 1 - с человекои; 2 - с ботом; => "))
        if  vibor==1 or vibor==2:
            break
    except ValueError:
        print()
if vibor == 1:
    while 1:
        print("Выберите одно из следующих значений ")
        print("1 - ножницы, 2 - бумага, 3 - камень")
        a=""
        while a!=int and a not in [1,2,3]:
            try:
                a=int(input("выберите номер: => "))
            except ValueError:
                print()
        if a==1:
            a=igra[0]
        elif a==2:
            a=igra[1]
        elif a==3:
            a=igra[2]
        b=""
        while a!=int and a not in [1,2,3]:
            try:
                a=int(input("выберите номер: => "))
            except ValueError:
                print()
        if b==1:
            b=igra[0]
        elif b==2:
            b=igra[1]
        elif b==3:
            b=igra[2]
        if a==b:
            print("Ничья")
        elif a == 1 and b == 2: 
            print("Победил Первый игрок!")
            results1.append(1)


