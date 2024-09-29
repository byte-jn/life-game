from weapons import weaponsgetaddon
import random as rd, time # importing various things

def createfight(player1, die, dieten, automode, enemylist, standartwartezeit, randommode, moa):
    if rd.randint(1,7) != 1:
                        time.sleep(standartwartezeit)
                        enemy = rd.choice(enemylist)
                        enemy["alter"] += rd.randint(0,30)
                        enemy["leben"] = int(float(enemy["leben"]) * (float(rd.randint(80 ,120))/100))
                        enemy = weaponsgetaddon(enemy,randommode)
                        enemy, player1 = fight(player1,enemy,die*dieten,automode, moa, standartwartezeit, randommode)
                        goblin1 = enemy
                        if enemy["leben"] < 1:
                            print(enemy["name"] + " has died, he was " + str(enemy["alter"]) + " years old.")
                            die += enemy["rank"] # die describes how many times someone has died, to later select the Demon King
                        print(" ")
                        print(" ")
    else:
                        time.sleep(standartwartezeit)
                        enemy1 = rd.choice(enemylist)
                        enemy1["alter"] += rd.randint(0,30)
                        enemy1["leben"] = int(float(enemy1["leben"]) * (float(rd.randint(80 ,120))/100))
                        enemy1 = weaponsgetaddon(enemy1,randommode)
                        enemy = rd.choice(enemylist)
                        enemy["alter"] += rd.randint(0,30)
                        enemy["leben"] = int(float(enemy["leben"]) * (float(rd.randint(80 ,120))/100))
                        enemy = weaponsgetaddon(enemy,randommode)
                        goblin1 = enemy
                        print(player1["name"] + " observes the fight between " + str(enemy["name"]) + " and " + str(enemy1["name"]))
                        print(" ")
                        print(" ")
                        enemy, enemy1 = fight(enemy,enemy1,die*dieten,"a",moa, standartwartezeit, randommode)
                        if enemy["leben"] < 1:
                            print(enemy["name"] + " has died; he was " + str(enemy["alter"]) + " years old.")
                        elif enemy1["leben"] < 1:
                            print(enemy1["name"] + " has died; he was " + str(enemy1["alter"]) + " years old.")
                        print(" ")
                        print(" ")
    return player1, enemy, goblin1 ,die

def fight(player1, gegner, die, a, moa, standartwartezeit, randommode):  # The fight
    automode = a
    if die > rd.randint(30, 301):
        gegner = moa  # random variable for the spawn of the Demon King
        print(player1["name"] + " fights against " + gegner["name"])  # Display for the fight
        print("The opponent has revealed himself as the Demon King.")
        
    if automode == "i":
        print("Do you want to fight against " + str(gegner["name"]) + " (HP: " + str(gegner["leben"]) + ")?")
    else:
        print(player1["name"] + " fights against " + gegner["name"])
        
    if rd.randint(1, 2) == 1:
        xs = True  # Who starts? Decision by chance
    else:
        xs = False
        
    if automode == "i":
        print("")
        time.sleep(standartwartezeit)
        print("Cheering gives the hero 2% more damage, but the opponent goes first.")
        print("Hints allow the hero to start, but the opponent deals more damage.")
        print("")
        print("Flee (f/n) / Fight (k/y) / Hint (h) / Cheer (a) / Weapon swap (w) / Chicken fight (c)")
        f = input()
        print("")
        
        if f == "f" or f == "n": 
            print("")
            print(player1["name"] + " flees from " + gegner["name"])
            print("")
            print("")
            return gegner
        elif f == "h":
            player1["attack-s"] = player1["attack-s"] / 1.2
            xs = True
        elif f == "w":
            player1 = weaponsgetaddon(player1, randommode)
            print(player1["name"] + " has a new weapon now.")
            print("")
        elif f == "a": 
            player1["attack-s"] = player1["attack-s"] * 1.2
            xs = False
        elif f == "c":
            player = player1
            player1 = {"name": "Chicken", "alter": 1, "leben": 5, "rank": 1}
            player1 = weaponsgetaddon(player1, randommode)
        print("")
        
    time.sleep(standartwartezeit)
    loopcount = 1
    loop = 0
    
    while True:  # Loop until someone dies
        loop += 1
        if gegner["leben"] < 1:  # Who won/lost
            print(player1["name"] + " has defeated " + gegner["name"])
            break
        elif player1["leben"] < 1:
            print(player1["name"] + " has lost to " + gegner["name"])
            break
            
        print("(" + player1["name"] + "-HP: " + str(player1["leben"]) + " / " + gegner["name"] + "-HP: " + str(gegner["leben"]) + ")")
        print(" ")
        time.sleep(standartwartezeit / (loop / 2))  # standard wait time :)
        
        if xs == True:  # Player1 hitting
            if loop >= 6:
                loopcount = loopcount * 2
            dmg = int(float(player1["attack-s"]) * (float(rd.randint(80, 120)) / float(100)) * loopcount)
            gegner["leben"] = gegner["leben"] - dmg
            print(player1["name"] + " " + player1["waffe"] + " " + gegner["name"] + ". And deals " + str(dmg) + " damage.")
            xs = False
        else:  # Opponent hitting
            dmg = int(float(gegner["attack-s"]) * (float(rd.randint(80, 120)) / float(100)) * loopcount)
            player1["leben"] = player1["leben"] - dmg
            print(gegner["name"] + " " + gegner["waffe"] + " " + player1["name"] + ". And deals " + str(dmg) + " damage.")
            xs = True
            
    if automode == "i":
        if f == "a":
            player1["attack-s"] = player1["attack-s"] / 1.2
        elif f == "h": 
            player1["attack-s"] = player1["attack-s"] * 1.2
        elif f == "c":
            player1 = player
            
    return gegner, player1  # Return all important info about the enemy
