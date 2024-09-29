def LifeGame():
    import random as rd, time # importing various things
    from fight import createfight
    from level_up import levelup
    from addon import addon
    from location import location
    from begin import begin

    standartwartezeit = 2 # standard waiting time :)
    moa = {"name": "The Demon King","alter": 24000,"attack-s": 90000000,"leben": 500000,"waffe": "schießt mit Atomic gegen", "rank": 10}

    player1, die, dieten, r, l, m, automode, randommode, standartwartezeit = begin(standartwartezeit)

    verblist, enemylist, locationslist = addon()

    while True:# Infinite repetition with some exceptions
        goblin1 = moa # goblin1 is the last opponent fought
        if goblin1["leben"] < 1 and goblin1["name"] == moa["name"]:# End if the Demon King dies
            print("")
            print(player1["name"] + " has won against " + goblin1["name"] + " gewonnen")
            print("Wait, What?")
            time.sleep(standartwartezeit)
            print("In any case, the world is now free")
            print("Thank you very much")
            break      
        if player1["leben"] < 1:# End if Player1 dies
            print("")
            print(player1["name"] + " was defeated. He was " + str(player1["alter"]) + " years old"),
            break
    
        player1["alter"] += 1
    
        location(verblist, enemylist, player1, locationslist, standartwartezeit)

        if rd.randint(r,25) > 15: # Fight
            player1, enemy, goblin1 ,die = createfight(player1, die, dieten, automode, enemylist, standartwartezeit, randommode, moa)
        if die > 0:
            if player1["leben"] > 0: # Regeneration for Player1
                if player1["leben"] < 1000000:
                    if player1["leben"] > 200:player1["leben"] += 5*r
                    else:player1["leben"] += 25*r
        if die > 15:
            die, dieten, player1, r, m, l = levelup(die,dieten,randommode,player1,standartwartezeit,r,m,l)
        time.sleep(standartwartezeit)

    time.sleep(10)

LifeGame()