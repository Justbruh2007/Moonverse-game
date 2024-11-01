import random
def shop (playerhp,guard,speed,attack,heal,cash):
    input("Привет, мои товарищи,у меня есть интересный товар,НО естественно не за бесплатно")
    input(f"У вас денег {cash}")
    while cash > 1500:
        buy = int(input(''' 1 - Бинт - 1500
        2 - Дополнительная броня Синдиката - 2500
        3 - Энкифалиновый модуль - 3000
        Ваш выбор: '''))
        if buy == 1:
            if boughtheal == 4:
                input("Торговец: У меня закончились бинты")
            else:
                heal = heal + 15
                cash = cash - 1500
                boughtheal = boughtheal + 1
        elif buy == 2:
            if boughtguard == 5:
                input("Торговец: У меня закончились материалы для брони")
            else:
                guard = guard + 1
                cash = cash - 2500
                boughtguard = boughtguard + 1
        elif buy == 3:
            if boughtmodule == 2:
                input("Торговец: У меня закончились модули")
            else:
                choose =  int(input('''На какие статы ты хочешь его применить
                                    1 - хп
                                    2 - скорость
                                    3 - аттака'''))
                if choose == 1:
                    playerhp = playerhp + 20
                    cash = cash - 3000
                    boughtmodule = boughtmodule + 1
                elif choose == 2:
                    extraspeed = extraspeed + 3
                    cash = cash - 3000
                    boughtmodule = boughtmodule + 1
                else:
                    attack = attack + 15
                    cash = cash - 3000
                    boughtmodule = boughtmodule + 1
    input("Скоро увидемся")
    return(playerhp,guard,speed,attack,heal,extraspeed)
