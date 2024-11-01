from data import *
from dialoges import name

def fight1(playerhp,attack,guard,crit,cash,totalhp):
    print('Ваша первая битва')
    enemy_hp = 150
    enemy_attack = 10
    speed = random.randint(1,6)
    luck = random.randint(1,5)
    while enemy_hp > 0:
        speed = random.randint(1,6)
        luck = random.randint(1,5)
        enemy_speed = random.randint(1,2)
        print(f'''{name} - {playerhp} хп
охранник - {enemy_hp} хп''')
        input()
        if speed > enemy_speed:
            if luck == crit:
                enemy_hp = enemy_hp - attack * 3
                input("Вы бьете врага, удачное попадение")
            else:
                enemy_hp = enemy_hp - attack + speed * 0.25
                input("Вы бьете врага")
        elif enemy_speed1 > speed:
            playerhp = playerhp + guard - enemy_attack
            input("Враг бьет вас")
        else:
            input("Ваши оружия скрипят по друг другу,но никто не наносит удар")
        if playerhp < 125:
            input("Остер: Вижу у тебя проблемы,дай помогу")
            playerhp = totalhp
            enemy_hp = 0
    coin_drop = random.randint(3500,3900)
    cash = coin_drop + cash
    input(f"Вы победили охраника,вы получили {coin_drop} монет")
    return (playerhp,attack,guard,crit,cash)

def fight2(playerhp,attack,guard,crit,cash,totalhp):
    print('Один из участников вас заметил')
    enemy_hp = 175
    enemy_attack = 15
    enemy_guard = 2
    enemy_crit = 2
    enemy_total =  175 
    while enemy_hp > 0:
        speed = random.randint(1,6)
        luck = random.randint(1,5)
        enemy_speed = random.randint(1,4)
        enemy_luck = random.randint(1,8)
        print(f'''{name} - {playerhp} хп
Враг - {enemy_hp} хп''')
        input()
        if speed > enemy_speed:
            if luck == crit:
                enemy_hp = enemy_hp - attack * 3
                input("Вы бьете врага, удачное попадение")
            else:
                enemy_hp = enemy_hp + enemy_guard - attack + speed * 0.25
                input("Вы бьете врага")
        elif enemy_speed > speed:
            if enemy_luck == enemy_crit:
                playerhp = playerhp - enemy_attack * 1.5
                input("Враг бьет вас,удачное попадение")
            else:
                playerhp = playerhp + guard - enemy_attack
                input("Враг бьет вас")
        else:
            input("Ваши оружия скрипят по друг другу,но никто не наносит удар")
        if playerhp < 1:
            playerhp = totalhp
            enemy_hp = enemy_total
            input('Перезапуск битвы')
    coin_drop = random.randint(4000,5500)
    cash = coin_drop + cash
    input(f"Вы победили члена синдиката 'Указательного пальца',вы получили {coin_drop} монет")
    return (playerhp,attack,guard,crit,cash)

def fight3(playerhp,attack,guard,crit,totalhp,extraspeed):
    print('Вы в ярости, от того что случилось')
    enemy_hp = 275
    enemy_attack = 30
    enemy_guard = 4
    enemy_crit = 1
    enemy_total =  275 
    while enemy_hp > 75:
        speed = random.randint(1,6)
        luck = random.randint(1,5)
        enemy_speed = random.randint(3,7)
        enemy_luck = random.randint(1,6)
        print(f'''{name} - {playerhp} хп
Враг - {enemy_hp} хп''')
        input()
        if speed + extraspeed > enemy_speed:
            if luck == crit:
                enemy_hp = enemy_hp - attack * 3
                input("Вы бьете врага, удачное попадение")
            else:
                enemy_hp = enemy_hp + enemy_guard - attack + speed * 0.25
                input("Вы бьете врага")
        elif enemy_speed > speed + extraspeed:
            if enemy_luck == enemy_crit:
                playerhp = playerhp - enemy_attack * 1.5
                input("Враг бьет вас,удачное попадение")
            else:
                playerhp = playerhp + guard - enemy_attack
                input("Враг бьет вас")
        else:
            input("Ваши оружия скрипят по друг другу,но никто не наносит удар")
        if playerhp < 1:
            playerhp = totalhp
            enemy_hp = enemy_total
            input('Перезапуск битвы')
    input("Элитный охраник: Нет, мне надо бежать включить сигнализацию,я не смогу справится с ним в одиночку")
    return (playerhp,attack,guard,crit,extraspeed)


def fight4(playerhp,attack,guard,crit,totalhp,extraspeed):
    print('На тебя напало 4 врага')
    enemys = 4
    for i in range(4):
        enemy_hp = random.randint(200,300)
        enemy_attack = random.randint(25,30)
        enemy_guard = 3
        enemy_crit = 2
        enemy_total =  enemy_hp
        while enemy_hp > 0:
            speed = random.randint(1,6)
            luck = random.randint(1,5)
            enemy_speed = random.randint(2,7)
            enemy_luck = random.randint(1,5)
            print(f'''{name} - {playerhp} хп
    Враг - {enemy_hp} хп''')
            input()
            if speed + extraspeed > enemy_speed:
                if luck == crit:
                    enemy_hp = enemy_hp - attack * 3
                    input("Вы бьете врага, удачное попадение")
                else:
                    enemy_hp = enemy_hp + enemy_guard - attack + speed * 0.25
                    input("Вы бьете врага")
            elif enemy_speed > speed + extraspeed:
                if enemy_luck == enemy_crit:
                    playerhp = playerhp - enemy_attack * 1.5
                    input("Враг бьет вас,удачное попадение")
                else:
                    playerhp = playerhp + guard - enemy_attack
                    input("Враг бьет вас")
            else:
                input("Ваши оружия скрипят по друг другу,но никто не наносит удар")
            if playerhp < 1:
                playerhp = totalhp
                enemy_hp = enemy_total
                input('Перезапуск битвы')
        enemys = enemys - 1
        input(f"У вас осталось {enemys} врагов на пути ")
    input("Вы победили")

    return (playerhp,attack,guard,crit,cash)


def fight5(playerhp,attack,guard,crit,totalhp,extraspeed):
    print('Вам нужно стать сильнее. . .')
    enemy_hp = 600
    enemy_attack = 35
    enemy_guard = 7
    enemy_crit = 4
    enemy_total =  600 
    while enemy_hp > 45:
        speed = random.randint(1,6)
        luck = random.randint(1,5)
        enemy_speed = random.randint(3,8)
        enemy_luck = random.randint (1,4)
        print(f'''{name} - {playerhp} хп
Хуберт - {enemy_hp} хп''')
        input()
        if speed + extraspeed > enemy_speed:
            if luck == crit:
                enemy_hp = enemy_hp - attack * 3
                input("Вы бьете Хуберта, удачное попадение")
                input("Вы: Я становлюсь сильнее. . .")
            else:
                enemy_hp = enemy_hp + enemy_guard - attack + speed * 0.5
                input("Вы бьете Хуберта")
                input("Вы: Я должен быть быстрее. . .")
        elif enemy_speed > speed + extraspeed:
            if playerhp < 70:
                input("Хуберт бьет вас,но Венглис вас защищает")
                input("Вы: Я должен защитить выживших,но не могу. . .")
            elif enemy_luck == enemy_crit:
                playerhp = playerhp - enemy_attack * 2
                input("Хуберт бьет вас,удачное попадение")
                input("Вы: Я должен стать сильнее. . .")
            else:
                playerhp = playerhp + guard - enemy_attack
                input("Хуберт бьет вас")
                input("Вы: Я должен одолеть его чтобы стать сильнейшим. . .")
        else:
            input("Ваши оружия скрипят по друг другу,но никто не наносит удар")
        if playerhp < 1:
            playerhp = totalhp
            enemy_hp = enemy_total
            input('Перезапуск битвы')
        extradmg = random.randint (45,75)
        enemy_hp = enemy_hp - extradmg
        input(f"Венглис дополнительно бьет Хуберта снося ему {extradmg}")
    input("'Хуберт использует сильную атаку и умирает,Венглис сильно ранен'")
    return (playerhp,attack,guard,crit,extraspeed)

def disort (disort_hp,disort_attack,disort_guard,disort_crit):
    enemy_hp = 600
    enemy_total = 600
    enemy_attack = 45
    enemy_guard = 10
    enemy_crit = 4
    eroison = 0
    disort_total = 400
    while enemy_hp > 100:
        speed = random.randint(3,7)
        luck = random.randint(1,5)
        enemy_speed = random.randint(2,7)
        enemy_luck = random.randint(1,4)
        print(f'''{name} - {playerhp} хп
Кало - {enemy_hp} хп''')
        input()
        if speed > enemy_speed:
            if luck == disort_crit:
                enemy_hp = enemy_hp - eroison + disort_attack * 3 
                input("Вы бьете врага, удачное попадение,вы чувствуете силу")
                eroison = eroison + 7
            else:
                enemy_hp = enemy_hp + enemy_guard - disort_attack + eroison
                input("Вы бьете врага,вы чувствуете силу")
                eroison = eroison + 3
        elif enemy_speed > speed:
            if enemy_luck == enemy_crit:
                disort_hp = disort_hp + eroison * 2 - enemy_attack * 2.5
                input("Кало бьет вас,удачное попадение,но вы почти не чувствуете боли")
            else:
                disort_hp = disort_hp + disort_guard - enemy_attack
                input("Кало бьет вас,но вы почти не чувствуете боли")
        else:
            input("Ваши оружия скрипят по друг другу,но никто не наносит удар")
        if disort_hp < 1:
            disort_hp = disort_total
            enemy_hp = enemy_total
        eroison = eroison - 1
        if eroison < 0:
            eroison = 0
    input("Вы победили главного в синдикате,вы стали на много сильнее")
def EGO (ego_hp,ego_attack,ego_guard,ego_crit):
    enemy_hp = 600
    enemy_total = 600
    enemy_attack = 45
    enemy_guard = 10
    enemy_crit = 4
    burn = 0
    ego_total = 300
    while enemy_hp > 100:
        speed = random.randint(3,8)
        luck = random.randint(1,3)
        enemy_speed = random.randint(2,7)
        enemy_luck = random.randint(1,4)
        print(f'''{name} - {playerhp} хп
Враг - {enemy_hp} хп''')
        input()
        if speed > enemy_speed:
            if luck == ego_crit:
                enemy_hp = enemy_hp - ego_attack * 3 
                input("Вы бьете врага,удачное попадание")
                burn = burn + 5
            else:
                enemy_hp = enemy_hp + enemy_guard - ego_attack
                input("Вы бьете врага")
                burn = burn + 2
        elif enemy_speed > speed:
            if enemy_luck == enemy_crit:
                ego_hp = ego_hp - enemy_attack * 1.5
                input("Кало бьет вас,удачное попадение")
            else:
                ego_hp = ego_hp + ego_guard - enemy_attack
                input("Кало бьет вас")
        else:
            input("Ваши оружия скрипят по друг другу,но никто не наносит удар")
        if ego_hp < 1:
            ego_hp = ego_total
            enemy_hp = enemy_total
        burn = burn - 1
        if burn < 0:
            burn = 0
    input("Вы победили главного в синдикате,ваша ЭГО успокаивается,броня пропадает и оружие становится нормальным")












def twofight1(playerhp,attack,guard,crit,cash,totalhp):
    print('Ваша первая битва')
    guard = 3
    enemy_hp = 150
    enemy_attack = 10
    speed = random.randint(1,6)
    luck = random.randint(1,5)
    while enemy_hp > 0:
        speed = random.randint(1,6)
        luck = random.randint(1,5)
        enemy_speed = random.randint(1,2)
        print(f'''{name} - {playerhp} хп
охранник - {enemy_hp} хп''')
        input()
        if speed > enemy_speed:
            if luck == crit:
                enemy_hp = enemy_hp - attack * 3
                input("Вы бьете врага, удачное попадение")
            else:
                enemy_hp = enemy_hp - attack
                input("Вы бьете врага")
        elif enemy_speed1 > speed:
            playerhp = playerhp + guard - enemy_attack
            input("Враг бьет вас")
        else:
            input("Ваши оружия скрипят по друг другу,но никто не наносит удар")
        if playerhp < 125:
            input("Остер: Вижу у тебя проблемы,дай помогу")
            playerhp = totalhp
            enemy_hp = 0
    coin_drop = random.randint(3500,3900)
    cash = coin_drop + cash
    input(f"Вы победили охраника,вы получили {coin_drop} монет")
    return (playerhp,attack,guard,crit,cash)

def twofight2(playerhp,attack,guard,crit,cash,totalhp):
    print('Один из участников вас заметил')
    guard = 3
    enemy_hp = 175
    enemy_attack = 15
    enemy_guard = 2
    enemy_crit = 2
    enemy_total =  175 
    while enemy_hp > 0:
        speed = random.randint(1,6)
        luck = random.randint(1,5)
        enemy_speed = random.randint(1,4)
        enemy_luck = random.randint(1,8)
        print(f'''{name} - {playerhp} хп
Враг - {enemy_hp} хп''')
        input()
        if speed > enemy_speed:
            if luck == crit:
                enemy_hp = enemy_hp - attack * 3
                input("Вы бьете врага, удачное попадение")
            else:
                enemy_hp = enemy_hp + enemy_guard - attack 
                input("Вы бьете врага")
        elif enemy_speed > speed:
            if enemy_luck == enemy_crit:
                playerhp = playerhp - enemy_attack * 1.5
                input("Враг бьет вас,удачное попадение")
            else:
                playerhp = playerhp + guard - enemy_attack
                input("Враг бьет вас")
        else:
            input("Ваши оружия скрипят по друг другу,но никто не наносит удар")
        if playerhp < 1:
            playerhp = totalhp
            enemy_hp = enemy_total
            input('Перезапуск битвы')
    coin_drop = random.randint(4000,5500)
    cash = coin_drop + cash
    input(f"Вы победили члена синдиката 'Указательного пальца',вы получили {coin_drop} монет")
    return (playerhp,attack,guard,crit,cash)

def twofight3(playerhp,attack,guard,crit,totalhp,extraspeed):
    print('Вы в ярости, от того что случилось')
    enemy_hp = 275
    enemy_attack = 30
    enemy_guard = 4
    enemy_crit = 1
    enemy_total =  275 
    while enemy_hp > 75:
        speed = random.randint(1,6)
        luck = random.randint(1,5)
        enemy_speed = random.randint(3,7)
        enemy_luck = random.randint(1,6)
        print(f'''{name} - {playerhp} хп
Враг - {enemy_hp} хп''')
        input()
        if speed + extraspeed > enemy_speed:
            if luck == crit:
                enemy_hp = enemy_hp - attack * 3
                input("Вы бьете врага, удачное попадение")
            else:
                enemy_hp = enemy_hp + enemy_guard - attack
                input("Вы бьете врага")
        elif enemy_speed > speed + extraspeed:
            if enemy_luck == enemy_crit:
                playerhp = playerhp - enemy_attack * 1.5
                input("Враг бьет вас,удачное попадение")
            else:
                playerhp = playerhp + guard - enemy_attack
                input("Враг бьет вас")
        else:
            input("Ваши оружия скрипят по друг другу,но никто не наносит удар")
        if playerhp < 1:
            playerhp = totalhp
            enemy_hp = enemy_total
            input('Перезапуск битвы')
    input("Элитный охраник: Нет, мне надо бежать включить сигнализацию,я не смогу справится с ним в одиночку")
    return (playerhp,attack,guard,crit,extraspeed)


def twofight4(playerhp,attack,guard,crit,totalhp,extraspeed):
    print('На тебя напало 4 врага')
    enemys = 4
    for i in range(4):
        enemy_hp = random.randint(200,300)
        enemy_attack = random.randint(25,30)
        enemy_guard = 3
        enemy_crit = 2
        enemy_total =  enemy_hp
        while enemy_hp > 0:
            speed = random.randint(1,6)
            luck = random.randint(1,5)
            enemy_speed = random.randint(2,7)
            enemy_luck = random.randint(1,5)
            print(f'''{name} - {playerhp} хп
    Враг - {enemy_hp} хп''')
            input()
            if speed + extraspeed > enemy_speed:
                if luck == crit:
                    enemy_hp = enemy_hp - attack * 3
                    input("Вы бьете врага, удачное попадение")
                else:
                    enemy_hp = enemy_hp + enemy_guard - attack
                    input("Вы бьете врага")
            elif enemy_speed > speed + extraspeed:
                if enemy_luck == enemy_crit:
                    playerhp = playerhp - enemy_attack * 1.5
                    input("Враг бьет вас,удачное попадение")
                else:
                    playerhp = playerhp + guard - enemy_attack
                    input("Враг бьет вас")
            else:
                input("Ваши оружия скрипят по друг другу,но никто не наносит удар")
            if playerhp < 1:
                playerhp = totalhp
                enemy_hp = enemy_total
                input('Перезапуск битвы')
        enemys = enemys - 1
        input(f"У вас осталось {enemys} врагов на пути ")
    input("Вы победили")

    return (playerhp,attack,guard,crit,cash)


def twofight5(playerhp,attack,guard,crit,totalhp,extraspeed):
    print('Вам нужно стать сильнее. . .')
    enemy_hp = 600
    enemy_attack = 35
    enemy_guard = 7
    enemy_crit = 4
    enemy_total =  600 
    while enemy_hp > 45:
        speed = random.randint(1,6)
        luck = random.randint(1,5)
        enemy_speed = random.randint(3,8)
        enemy_luck = random.randint (1,4)
        print(f'''{name} - {playerhp} хп
Хуберт - {enemy_hp} хп''')
        input()
        if speed + extraspeed > enemy_speed:
            if luck == crit:
                enemy_hp = enemy_hp - attack * 3
                input("Вы бьете Хуберта, удачное попадение")
                input("Вы: Я становлюсь сильнее. . .")
            else:
                enemy_hp = enemy_hp + enemy_guard - attack
                input("Вы бьете Хуберта")
                input("Вы: Я должен быть быстрее. . .")
        elif enemy_speed > speed + extraspeed:
            if playerhp < 70:
                input("Хуберт бьет вас,но Венглис вас защищает")
                input("Вы: Я должен защитить выживших,но не могу. . .")
            elif enemy_luck == enemy_crit:
                playerhp = playerhp - enemy_attack * 2
                input("Хуберт бьет вас,удачное попадение")
                input("Вы: Я должен стать сильнее. . .")
            else:
                playerhp = playerhp + guard - enemy_attack
                input("Хуберт бьет вас")
                input("Вы: Я должен одолеть его чтобы стать сильнейшим. . .")
        else:
            input("Ваши оружия скрипят по друг другу,но никто не наносит удар")
        if playerhp < 1:
            playerhp = totalhp
            enemy_hp = enemy_total
            input('Перезапуск битвы')
        extradmg = random.randint (45,75)
        enemy_hp = enemy_hp - extradmg
        input(f"Венглис дополнительно бьет Хуберта снося ему {extradmg}")
    input("'Хуберт использует сильную атаку и умирает,Венглис сильно ранен'")
    return (playerhp,attack,guard,crit,extraspeed)








def threefight1(playerhp,attack,guard,crit,cash,totalhp):
    print('Ваша первая битва')
    enemy_hp = 150
    enemy_attack = 10
    speed = random.randint(1,6)
    luck = random.randint(1,5)
    while enemy_hp > 0:
        speed = random.randint(1,6)
        luck = random.randint(1,3)
        enemy_speed = random.randint(1,2)
        print(f'''{name} - {playerhp} хп
охранник - {enemy_hp} хп''')
        input()
        if speed > enemy_speed:
            if luck == crit:
                enemy_hp = enemy_hp - attack * 2
                input("Вы бьете врага, удачное попадение")
            else:
                enemy_hp = enemy_hp - attack
                input("Вы бьете врага")
        elif enemy_speed1 > speed:
            playerhp = playerhp + guard - enemy_attack
            input("Враг бьет вас")
        else:
            input("Ваши оружия скрипят по друг другу,но никто не наносит удар")
        if playerhp < 125:
            input("Остер: Вижу у тебя проблемы,дай помогу")
            playerhp = totalhp
            enemy_hp = 0
    coin_drop = random.randint(3500,3900)
    cash = coin_drop + cash
    input(f"Вы победили охраника,вы получили {coin_drop} монет")
    return (playerhp,attack,guard,crit,cash)

def threefight2(playerhp,attack,guard,crit,cash,totalhp):
    print('Один из участников вас заметил')
    enemy_hp = 175
    enemy_attack = 15
    enemy_guard = 2
    enemy_crit = 2
    enemy_total =  175 
    while enemy_hp > 0:
        speed = random.randint(1,6)
        luck = random.randint(1,3)
        enemy_speed = random.randint(1,4)
        enemy_luck = random.randint(1,8)
        print(f'''{name} - {playerhp} хп
Враг - {enemy_hp} хп''')
        input()
        if speed > enemy_speed:
            if luck == crit:
                enemy_hp = enemy_hp - attack * 2
                input("Вы бьете врага, удачное попадение")
            else:
                enemy_hp = enemy_hp + enemy_guard - attack
                input("Вы бьете врага")
        elif enemy_speed > speed:
            if enemy_luck == enemy_crit:
                playerhp = playerhp - enemy_attack * 1.5
                input("Враг бьет вас,удачное попадение")
            else:
                playerhp = playerhp + guard - enemy_attack
                input("Враг бьет вас")
        else:
            input("Ваши оружия скрипят по друг другу,но никто не наносит удар")
        if playerhp < 1:
            playerhp = totalhp
            enemy_hp = enemy_total
            input('Перезапуск битвы')
    coin_drop = random.randint(4000,5500)
    cash = coin_drop + cash
    input(f"Вы победили члена синдиката 'Указательного пальца',вы получили {coin_drop} монет")
    return (playerhp,attack,guard,crit,cash)

def threefight3(playerhp,attack,guard,crit,totalhp,extraspeed):
    print('Вы в ярости, от того что случилось')
    enemy_hp = 275
    enemy_attack = 30
    enemy_guard = 4
    enemy_crit = 1
    enemy_total =  275 
    while enemy_hp > 75:
        speed = random.randint(1,6)
        luck = random.randint(1,3)
        enemy_speed = random.randint(3,7)
        enemy_luck = random.randint(1,6)
        print(f'''{name} - {playerhp} хп
Враг - {enemy_hp} хп''')
        input()
        if speed + extraspeed > enemy_speed:
            if luck == crit:
                enemy_hp = enemy_hp - attack * 2
                input("Вы бьете врага, удачное попадение")
            else:
                enemy_hp = enemy_hp + enemy_guard - attack
                input("Вы бьете врага")
        elif enemy_speed > speed + extraspeed:
            if enemy_luck == enemy_crit:
                playerhp = playerhp - enemy_attack * 1.5
                input("Враг бьет вас,удачное попадение")
            else:
                playerhp = playerhp + guard - enemy_attack
                input("Враг бьет вас")
        else:
            input("Ваши оружия скрипят по друг другу,но никто не наносит удар")
        if playerhp < 1:
            playerhp = totalhp
            enemy_hp = enemy_total
            input('Перезапуск битвы')
    input("Элитный охраник: Нет, мне надо бежать включить сигнализацию,я не смогу справится с ним в одиночку")
    return (playerhp,attack,guard,crit,extraspeed)


def threefight4(playerhp,attack,guard,crit,totalhp,extraspeed):
    print('На тебя напало 4 врага')
    enemys = 4
    for i in range(4):
        enemy_hp = random.randint(200,300)
        enemy_attack = random.randint(25,30)
        enemy_guard = 3
        enemy_crit = 2
        enemy_total =  enemy_hp
        while enemy_hp > 0:
            speed = random.randint(1,6)
            luck = random.randint(1,3)
            enemy_speed = random.randint(2,7)
            enemy_luck = random.randint(1,5)
            print(f'''{name} - {playerhp} хп
    Враг - {enemy_hp} хп''')
            input()
            if speed + extraspeed > enemy_speed:
                if luck == crit:
                    enemy_hp = enemy_hp - attack * 2
                    input("Вы бьете врага, удачное попадение")
                else:
                    enemy_hp = enemy_hp + enemy_guard - attack
                    input("Вы бьете врага")
            elif enemy_speed > speed + extraspeed:
                if enemy_luck == enemy_crit:
                    playerhp = playerhp - enemy_attack * 1.5
                    input("Враг бьет вас,удачное попадение")
                else:
                    playerhp = playerhp + guard - enemy_attack
                    input("Враг бьет вас")
            else:
                input("Ваши оружия скрипят по друг другу,но никто не наносит удар")
            if playerhp < 1:
                playerhp = totalhp
                enemy_hp = enemy_total
                input('Перезапуск битвы')
        enemys = enemys - 1
        input(f"У вас осталось {enemys} врагов на пути ")
    input("Вы победили")

    return (playerhp,attack,guard,crit,cash)


def threefight5(playerhp,attack,guard,crit,totalhp,extraspeed):
    print('Вам нужно стать сильнее. . .')
    enemy_hp = 600
    enemy_attack = 35
    enemy_guard = 7
    enemy_crit = 4
    enemy_total =  600 
    while enemy_hp > 45:
        speed = random.randint(1,6)
        luck = random.randint(1,3)
        enemy_speed = random.randint(3,8)
        enemy_luck = random.randint (1,4)
        print(f'''{name} - {playerhp} хп
Хуберт - {enemy_hp} хп''')
        input()
        if speed + extraspeed > enemy_speed:
            if luck == crit:
                enemy_hp = enemy_hp - attack * 2
                input("Вы бьете Хуберта, удачное попадение")
                input("Вы: Я становлюсь сильнее. . .")
            else:
                enemy_hp = enemy_hp + enemy_guard - attack
                input("Вы бьете Хуберта")
                input("Вы: Я должен быть быстрее. . .")
        elif enemy_speed > speed + extraspeed:
            if playerhp < 70:
                input("Хуберт бьет вас,но Венглис вас защищает")
                input("Вы: Я должен защитить выживших,но не могу. . .")
            elif enemy_luck == enemy_crit:
                playerhp = playerhp - enemy_attack * 2
                input("Хуберт бьет вас,удачное попадение")
                input("Вы: Я должен стать сильнее. . .")
            else:
                playerhp = playerhp + guard - enemy_attack
                input("Хуберт бьет вас")
                input("Вы: Я должен одолеть его чтобы стать сильнейшим. . .")
        else:
            input("Ваши оружия скрипят по друг другу,но никто не наносит удар")
        if playerhp < 1:
            playerhp = totalhp
            enemy_hp = enemy_total
            input('Перезапуск битвы')
        extradmg = random.randint (45,75)
        enemy_hp = enemy_hp - extradmg
        input(f"Венглис дополнительно бьет Хуберта снося ему {extradmg}")
    input("'Хуберт использует сильную атаку и умирает,Венглис сильно ранен'")
    return (playerhp,attack,guard,crit,extraspeed)

    