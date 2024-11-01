from dialoges import *
from battle1 import *
from shop import *

dialoge1()

choose = int(input())
if choose == 1:
    input(f"Вы: Ранга")
elif choose == 2:
    input(f"Вы: Аллас")
else:
    input(f"Вы: Дуррандал")

dialoge1dot5()

if choose == 1:
    fight1(playerhp,attack,guard,crit,cash,totalhp)
    playerhp = playerhp + heal
    totalhp =  playerhp

    dialoge2()

    fight2(playerhp,attack,guard,crit,cash,totalhp)
    playerhp = playerhp + heal
    totalhp =  playerhp

    dialoge3()

    shop(playerhp,guard,speed,attack,heal,cash)

    dialoge4()

    fight3(playerhp,attack,guard,crit,totalhp,extraspeed)

    dialoge5()

    fight4(playerhp,attack,guard,crit,totalhp,extraspeed)

    dialoge6()

    fight5(playerhp,attack,guard,crit,totalhp,extraspeed)

    dialoge7()

    choose2 = int(input(''' 1 - Согласиться
2 - отказаться'''))
    if choose2 == 1:
        disort1()

        disort(disort_hp,disort_attack,disort_guard,disort_crit)

        disort2()
    else:
        ego1()

        EGO(ego_hp,ego_attack,ego_guard,ego_crit)

        ego2()
    
if choose == 2:
    twofight1(playerhp,attack,guard,crit,cash,totalhp)
    playerhp = playerhp + heal
    totalhp =  playerhp

    dialoge2()

    twofight2(playerhp,attack,guard,crit,cash,totalhp)
    playerhp = playerhp + heal
    totalhp =  playerhp

    dialoge3()

    shop(playerhp,guard,speed,attack,heal,cash)

    dialoge4()

    twofight3(playerhp,attack,guard,crit,totalhp,extraspeed)

    dialoge5()

    twofight4(playerhp,attack,guard,crit,totalhp,extraspeed)

    dialoge6()

    twofight5(playerhp,attack,guard,crit,totalhp,extraspeed)

    dialoge7()

    choose2 = int(input(''' 1 - Согласиться
2 - отказаться'''))
    if choose2 == 1:
        disort1()

        disort(disort_hp,disort_attack,disort_guard,disort_crit)

        disort2()
    else:
        ego1()

        EGO(ego_hp,ego_attack,ego_guard,ego_crit)

        ego2()
    
else:
    threefight1(playerhp,attack,guard,crit,cash,totalhp)
    playerhp = playerhp + heal
    totalhp =  playerhp

    dialoge2()

    threefight2(playerhp,attack,guard,crit,cash,totalhp)
    playerhp = playerhp + heal
    totalhp =  playerhp

    dialoge3()

    shop(playerhp,guard,speed,attack,heal,cash)

    dialoge4()

    threefight3(playerhp,attack,guard,crit,totalhp,extraspeed)

    dialoge5()

    threefight4(playerhp,attack,guard,crit,totalhp,extraspeed)

    dialoge6()

    threefight5(playerhp,attack,guard,crit,totalhp,extraspeed)

    dialoge7()

    choose2 = int(input(''' 1 - Согласиться
2 - отказаться'''))
    if choose2 == 1:
        disort1()

        disort(disort_hp,disort_attack,disort_guard,disort_crit)

        disort2()
    else:
        ego1()

        EGO(ego_hp,ego_attack,ego_guard,ego_crit)

        ego2()