from random import*
from keyboard import* 
igra = ["ножницы","бумага","камень"]
results1 =[]
results2 =[]
print("************************** Добро пожаловать в игру! **************************")
print("********************************** Правила ***********************************")
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
        b=""
        while b!=int and b not in [1,2,3]:
            try:
                b=int(input("выберите номер: => "))
            except ValueError:
                print()
        if a == b:
            print("Ничья")
        elif a == 1 and b == 2: #Player1 - a and Player2 - b 
            print("Победил Первый игрок!" )
            results1.append(1)
        elif a == 1 and b == 3:
            print("Победил Второй игрок!")
            results2.append(1)
        elif a == 2 and b == 3:
            print("Победил Первый игрок!")
            results1.append(1)
        elif a == 2 and b == 1:
            print ("Победил Второй игрок!")
            results2.append(1)
        elif a == 3 and b == 1:
            print("Победил Первый игрок!")
            results1.append(1)
        elif a == 3 and b == 2:
            print("Победил Второй игрок!")
            results2.append(1)
        User1=sum(results1)
        User2=sum(results2)
        print(User1, User2)
        print()
        if User1 % 10 == 0 or User2 % 10 == 0 and User1!=0 or User2!=0:
            while 1: 
                try:
                    trash=int(input("Обнуляем счет?  1 -да; 2 - нет; => "))
                    if  trash==1 or trash==2:
                        break
                except ValueError:
                    print()
            if trash == 1:
                results1.clear()
                results2.clear()
        print()


            


