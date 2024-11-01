import random

#игрок
totalhp = 250
playerhp = 250
attack = 15
guard = 2
speed = random.randint(1,6)
luck = random.randint(1,5)
crit = 1
cash = 1
heal = 125
extraspeed = 1






#Охраник
enemy_total1 = 150
enemy_hp1 = 150
enemy_attack1 = 20
enemy_speed1 = random.randint(1,4)
coin_drop = random.randint(2500,3750)

#вторая битва
enemy_total2 =  175 
enemy_hp2 = 175
enemy_attack2 = 25
enemy_guard2 = 3
enemy_speed2 = random.randint(1,5)
enemy_luck2 = random.randint(1,6)
enemy_crit2 = 2
coin_drop = random.randint(3000,4500)

#Третья битва
enemy_hp3 = 275
enemy_attack3 = 37.5
enemy_guard3 = 5
enemy_speed3 = random.randint(2,6)
enemy_luck3 = random.randint(2,6)
enemy_crit = 3
#если у врага становится меньше 75 хп то бой заканчивается

#Четвертая битва (планируется около 4 битв подряд с одинаковыми характеристиками)
enemy_hp4 = 235
enemy_attack4 = 30
enemy_guard4 = 4
enemy_speed3 = random.randint(3,5)
enemy_luck3 = random.randint(1,6)
enemy_crit = 6


#Первый босс
boss_hp = 500
boss_attack = 40
boss_guard = 6
boss_speed =  random.randint(2,7)
boss_luck = random.randint (1,4)
boss_crit = 4

#Финальный босс
boss_hp2 = 600
boss_attack = 45
boss_guard = 7
boss_crit = 4
boss_speed =  random.randint(2,7)
boss_luck = random.randint (1,4)

#Искажения
disort_hp = 400
disort_attack = 35
disort_guard = 7
disort_speed = random.randint(1,7)
disort_luck = random.randint(1,4)
disort_crit = 4
#Будет 2 искажения от выбора игрока,у которых будут разные пассивные способности
#Защита и ерозия
#Защита - чем меньше хп - тем больше защита (защита увеличивается на 3 за каждые потеряные 100 хп)
#Еросия -  при каждом ударе по боссу на него будет накладываться ерозия которая увеличивает наносимый урон по боссу на (колличество ерозии * 0.25 )

#ЭГО
ego_hp = 300
ego_attack = 35
ego_guard = 5
ego_crit = 3
ego_speed = random.randint(3,8)
ego_luck = random.randint(1,3)
#Будет 2 эго от выбора игрока,у которых будут разные пассивные способности
#Ожог и Берсерк
#Ожог - при удачном ударе по боссу наносит на него эффект ожога который после хода наносит боссу урон равный количеству ожога (ожог уменьшается на 1 после каждого хода)
#Берсерк - чем меньше хп тем больше урона ( урон увеличивается на 5 за каждые потеряные 50 хп)
