import random 
import getpass 
igra = ["ножницы","бумага","камень"]
results1 =[]
results2 =[]
print("************************** Добро пожаловать в игру! **************************")
print("********************************** Правила ***********************************")
print("Все предельно просто: Выбираем тип игры (с ИИ или человеком), Выбираем одно из 3-ех действий и смотрим кто кого победил")
print("1)Ножницы бьют бумагу. 2)Камень бьет ножницы. 3)Бумага бьет камень.")
print("При игре человек против человека будут скрыты все символы введенные игроком!")
print("П.С. Про баг с текстом при игре человек против человека, даже не пишите, разрабы библиотеки Getpass не чинили ее")
print()
print("********************************** Начнем! ***********************************")
print()
while 1: 
    try:
        vibor=int(input("Будете играть с человеком или ботом. 1 - с человекои; 2 - с ботом; => "))
        if  vibor==1 or vibor==2:
            break
    except ValueError:
        print()
print()
if vibor == 1:
    name1=input("Имя первого игрока: => ")
    print()
    name2=input("Имя второго игрока: => ")
    while 1:
        print("Выберите одно из следующих значений")
        print("1 - ножницы, 2 - бумага, 3 - камень")
        print()
        a=""
        while a!=int and a not in [1,2,3]:
            try:
                a=int(getpass.getpass(prompt=f'*******Ходит {name1} =>', stream= None ))
            except ValueError:
                print("Error, try again: ")
        b=""
        while b!=int and b not in [1,2,3]:
            try:
                b=int(getpass.getpass(prompt=f'*******Ходит {name2} =>', stream= None ))
            except ValueError:
                print("Error, try again: ")
        if a == b:
            print("Ничья")
            print()
        elif a == 1 and b == 2: #Player1 - a and Player2 - b 
            print("Победил", name1, "!")
            results1.append(1)
            print()
        elif a == 1 and b == 3:
            print("Победил", name2,"!")
            results2.append(1)
            print()
        elif a == 2 and b == 3:
            print("Победил", name1,"!")
            results1.append(1)
            print()
        elif a == 2 and b == 1:
            print ("Победил", name2,"игрок!")
            results2.append(1)
            print()
        elif a == 3 and b == 1:
            print("Победил", name1, "!")
            results1.append(1)
            print()
        elif a == 3 and b == 2:
            print("Победил", name2, "игрок!")
            results2.append(1)
            print()
        User1=sum(results1)
        User2=sum(results2)
        print()
        print(name1,"-", User1, "|", name2,"-", User2)
        print("__________________________________________________")
        if User1 % 10 == 0  and User1!=0 :
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
        elif User2 % 10 == 0  and User2!=0 :
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
if vibor == 2:
    name3=input("Имя игрока: => ")
    print()
    while 1:
        print("Выберите одно из следующих значений:")
        print("1 - ножницы, 2 - бумага, 3 - камень")
        player1=""
        while player1!=int and player1 not in [1,2,3]:
            try:
                player1=int(input(f"Выбирай {name3}: => "))
            except ValueError:
                print()
        if player1 == 1:
            player1 = "ножницы"
        elif player1 == 2:
            player1 = "бумага"
        elif player1 == 3:
            player1 ="камень"
        bot=random.choice(igra)
        print()
        print("Бот выбрал:", bot)
        if player1 == bot:
            print("Ничья")
            print()
        elif player1 == "ножницы" and bot == "бумага": 
            print("Победил", name3, "!")
            results1.append(1)
            print()
        elif player1 == "ножницы" and bot == "камень":
            print("Победил бот!")
            results2.append(1)
            print()
        elif player1 == "бумага" and bot == "камень":
            print("Победил", name3, "!")
            results1.append(1)
            print()
        elif player1 == "бумага" and bot == "ножницы":
            print ("Победил бот!")
            results2.append(1)
            print()
        elif player1 == "камень" and bot == "ножницы":
            print("Победил", name3, "!")
            results1.append(1)
            print()
        elif player1 == "камень" and bot == "бумага":
            print("Победил бот!")
            results2.append(1)
            print()
        User3=sum(results1)
        User4=sum(results2)
        print()
        print(name3,"-", User3,"| Бот - ", User4)
        print("__________________________________________________")
        if User3 % 10 == 0  and User3!=0 :
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
        elif User4 % 10 == 0  and User4!=0 :
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