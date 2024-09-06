import random as rd, time #importieren von verschiedensten Sachen
from fight import createfight
from level_up import levelup
from addon import addon
from location import location
from begin import begin

standartwartezeit = 2 #standart wartezeit :)
moa = {"name": "Der Dämonenkönig","alter": 24000,"attack-s": 90000000,"leben": 500000,"waffe": "schießt mit Atomic gegen", "rank": 10}

player1, die, dieten, r, l, m, automode, randommode, standartwartezeit = begin(standartwartezeit)

verblist, enemylist, locationslist = addon()

while True:# Wiederholung Unendlich mit einigen außnahmen
    goblin1 = moa #goblin1 ist der letze gegen den man gespielt hat
    if goblin1["leben"] < 1 and goblin1["name"] == moa["name"]:#Ende wenn der Dämonenkönig stirbt
        print("")
        print(player1["name"] + " hat gegen den " + goblin1["name"] + " gewonnen")
        print("Warte. Was!? Wie!?")
        time.sleep(standartwartezeit)
        print("Auf Jeden Fall ist die Welt jetzt befreit")
        print("Vielen Dank")
        break      
    if player1["leben"] < 1:#Ende wenn Player1 stirbt
        print("")
        print(player1["name"] + " wurde besiegt er war " + str(player1["alter"]) + " jahre alt"),
        break
    
    player1["alter"] += 1
    
    location(verblist, enemylist, player1, locationslist, standartwartezeit)

    if rd.randint(r,25) > 15: #Kampf
        player1, enemy, goblin1 ,die = createfight(player1, die, dieten, automode, enemylist, standartwartezeit, randommode, moa)
    if die > 0:
        if player1["leben"] > 0: #Regenerierung Player1
            if player1["leben"] < 1000000:
                if player1["leben"] > 200:player1["leben"] += 5*r
                else:player1["leben"] += 25*r
    if die > 15:
        die, dieten, player1, r, m, l = levelup(die,dieten,randommode,player1,standartwartezeit,r,m,l)
    time.sleep(standartwartezeit)

time.sleep(10)
