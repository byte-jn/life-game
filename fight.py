from weapons import weaponsgetaddon
import random as rd, time #importieren von verschiedensten Sachen

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
                            print(enemy["name"] + " ist gestorben er war " + str(enemy["alter"]) + " Jahre alt")
                            die += enemy["rank"] #die beschreibt wie oft jemand schon gestorben sind. Um später dann den Dämonenkönig auszuwählen
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
                        print(player1["name"] + " beobachtet kampf zwischen " + str(enemy["name"]) + " und " + str(enemy1["name"]))
                        print(" ")
                        print(" ")
                        enemy, enemy1 = fight(enemy,enemy1,die*dieten,"a",moa, standartwartezeit, randommode)
                        if enemy["leben"] < 1:
                            print(enemy["name"] + " ist gestorben er war " + str(enemy["alter"]) + " Jahre alt")
                        elif enemy1["leben"] < 1:
                            print(enemy1["name"] + " ist gestorben er war " + str(enemy1["alter"]) + " Jahre alt")
                        print(" ")
                        print(" ")
    return player1, enemy, goblin1 ,die


def fight(player1,gegner,die, a, moa, standartwartezeit, randommode):#Der Kampf
            automode = a
            if die > rd.randint(30,301):
                gegner = moa #zufällige Variable für den Spawn des Dämonenkönigs
                print(player1["name"] + " kämpft gegen " + gegner["name"])#Anzeige für den Kampf
                print("Gegner hat sich als Dämonenkönig entpupt")
            else:
                if automode == "e":
                    print("Willst du gegen " + str(gegner["name"]) + " kämpfen?")#Anzeige für den Kampf
                else:
                    print(player1["name"] + " kämpft gegen " + gegner["name"])#Anzeige für den Kampf
            if rd.randint(1,2) == 1:xs = True #Wer fängt an? Entscheidung durch Zufall
            else: xs = False
            if automode == "e":
                print("")
                time.sleep(standartwartezeit)
                print("Anfeuern gibt dem Helden 2% mehr schaden, aber der Gegner fängt an")
                print("Hinweisen lässt den Helden an fangen, aber der Gegner macht mehr schaden")
                print("")
                print("fliehen (f/n) / kämpfen (k/j) / hinweisen (h) / anfeuern (a) / waffetausch (w) / Huhn Kampf (c)")
                f = input()
                print("")
                if f == "f" or f == "n": 
                    print("")
                    print(player1["name"] + " flieht vor " + gegner["name"])
                    print("")
                    print("")
                    return gegner
                elif f == "h":
                    player1["attack-s"] = player1["attack-s"] / 1.2
                    xs = True
                elif f == "w":
                    player1 = weaponsgetaddon(player1, randommode)
                    print(player1["name"] + " hat jetzt eine neue Waffe")
                    print("")
                elif f == "a": 
                    player1["attack-s"] = player1["attack-s"] * 1.2
                    xs = False
                elif f == "c":
                    player = player1
                    player1 = {"name": "Huhn", "alter": 1, "leben": 5, "rank": 1}
                    player1 = weaponsgetaddon(player1, randommode)
                print("")
            time.sleep(standartwartezeit)
            loopcount = 1
            loop = 0
            while True:#Loop bis Jemand tod ist
                loop += 1
                if gegner["leben"] < 1:#Wer gewonnen/verloren hat
                    print(player1["name"] + " hat gegen " + gegner["name"] + " gewonnen")
                    break
                elif  player1["leben"] < 1:
                    print(player1["name"] + " hat gegen " + gegner["name"] + " verloren")
                    break
                print("(" + player1["name"] + "-HP: " + str(player1["leben"]) + " / " + gegner["name"] + "-HP: " + str(gegner["leben"]) + ")")
                print(" ")
                time.sleep(standartwartezeit/(loop/2))#standart wartezeit :)
                if xs == True:#Player1 schlägt zu
                    if loop >= 6:
                        loopcount = loopcount*2
                    dmg = int(float(player1["attack-s"])*(float(rd.randint(80,120))/float(100))*loopcount)
                    gegner["leben"] = gegner["leben"] - dmg
                    print( player1["name"] + " " + player1["waffe"] + " " + gegner["name"] + ". Und macht " + str(dmg) + " Schaden")
                    xs = False
                else:#Gegner schlägt zu
                    dmg = int(float(gegner["attack-s"])*(float(rd.randint(80,120))/float(100))*(float(loopcount)/1000))
                    player1["leben"] = player1["leben"] - dmg
                    print( gegner["name"] + " " + gegner["waffe"] + " " + player1["name"] + ". Und macht " + str(dmg) + " Schaden")
                    xs = True
            if automode == "e":
                if f == "a":
                    player1["attack-s"] = player1["attack-s"] / 1.2
                elif f == "h": 
                    player1["attack-s"] = player1["attack-s"] * 1.2
                elif f == "c":
                    player1 = player
            return gegner, player1 #Alle wichtigen Infos vom gegner zurück geben