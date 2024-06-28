import random as rd, time #importieren von verschiedensten Sachen
import json

standartwartezeit = 2 #standart wartezeit :)
class LifeGameMain:#Alle wichtigen abläufe in dieser class
        def weaponsgetaddon(object1): 
            with open("weapondmg.json") as f:
                weapon_data = json.load(f)
                weaponlist = weapon_data[0]  # Access the dictionary within the list
            
            weaponlist = lg.replace_umlauts(weaponlist)

            if randommode == "r":
                if object1["rank"] < 11:
                    weapon_rank_key = f"r{rd.randint(1,10)}"
                    if weapon_rank_key in weaponlist:
                        rank_weaponlist = weaponlist[weapon_rank_key]
                        weapon = rd.choice(rank_weaponlist)
                    else:
                        raise ValueError(f"Rank {rd.randint(1,10)} not found in weaponlist")
                else:
                    weapon = {
                        "name": "Macht der Unendlichkeit",
                        "waffe": "schoß mit der Magie der Unendlichkeit auf",
                        "attack-s": 1000000000000
                    }
            else:
                if object1["rank"] < 11:
                    weapon_rank_key = f"r{object1['rank']}"
                    if weapon_rank_key in weaponlist:
                        rank_weaponlist = weaponlist[weapon_rank_key]
                        weapon_rank_key_true = True
                        a = 0
                        while weapon_rank_key_true == True:
                            a += 1
                            weapon_rank_key = f"r{object1['rank']-a}"
                            if weapon_rank_key in weaponlist:
                                rank_weaponlist = rank_weaponlist + weaponlist[weapon_rank_key]
                            else: 
                                weapon_rank_key_true = False
                        weapon = rd.choice(rank_weaponlist)
                    else:
                        raise ValueError(f"Rank {object1['rank']} not found in weaponlist")
                else:
                    weapon = {
                        "name": "Macht der Unendlichkeit",
                        "waffe": "schoß mit der Magie der Unendlichkeit auf",
                        "attack-s": 1000000000000
                    }

            object1 = {
                "name": object1["name"],
                "alter": object1["alter"],
                "attack-s": weapon["attack-s"],
                "leben": object1["leben"],
                "waffe": weapon["waffe"],
                "rank": object1["rank"]
            }
            
            return object1
        def fight(player1,gegner,die):#Der Kampf
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
                time.sleep(2)
                print("Anfeuern gibt dem Helden 2% mehr schaden, aber der Gegner fängt an")
                print("Hinweisen lässt den Helden an fangen, aber der Gegner macht mehr schaden")
                print("")
                print("fliehen (f/n) / kämpfen (k/j) / hinweisen (h) / anfeuern (a) / waffetausch (w)")
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
                    if rd.randint (1,3) == 1:
                        xs = False
                    else:
                        xs = True
                elif f == "w":
                    player1 = lg.weaponsgetaddon(player1)
                    print(player1["name"] + " hat jetzt eine neue Waffe")
                    print("")
                elif f == "a": 
                    player1["attack-s"] = player1["attack-s"] * 1.2
                print("")
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
                time.sleep(standartwartezeit)#standart wartezeit :)
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
            return gegner #Alle wichtigen Infos vom gegner zurück geben
        def replace_umlauts(data):
            if isinstance(data, str):
                data = (data.replace("(Ae)", "Ä")
                            .replace("(ae)", "ä")
                            .replace("(Oe)", "Ö")
                            .replace("(oe)", "ö")
                            .replace("(Ue)", "Ü")
                            .replace("(ue)", "ü")
                            .replace("(sz)", "ß"))
            elif isinstance(data, dict):
                for key, value in data.items():
                    data[key] = lg.replace_umlauts(value)
            elif isinstance(data, list):
                for i in range(len(data)):
                    data[i] = lg.replace_umlauts(data[i])
            return data

lg = LifeGameMain #class in eine einfache Variable packen um darauf einfach zugreifen zu können

print("Gebe einen Namen ein... ")
name = input()
print(" ")

print("Wie stark willst du sein? (s/a/b/c/d/e/f)?")
m = input("Stärke = ")

print("")
print("Automode lässt dich automatisch kämpfen und nicht auswählen was du machen willst.")
print("Bei Eingabe kannst du auswählen ob du fliehen willst oder kämpfen möchtest und mehr.")
print("Automode (a) / Eingabe (e)...")
global automode
automode = input("Mode = ")

print("")
print("Random (r) / normal (n)")
global randommode
randommode = input("Mode = ")

if randommode != "r":
    if m in {"dev","sss","ss","s", "a", "b", "c", "d", "e", "f"}:
        match m:
            case "dev": 
                r = 10
                l = 10000
                standartwartezeit = 0.2
            case "sss": 
                r = 9
                l = 1000
            case "ss": 
                r = 8
                l = 100
            case "s": 
                r = 7
                l = 10
            case "a": 
                r = 6
                l = 5
            case "b": 
                r = 5
                l = 2
            case "c": 
                r = 4
                l = 1.5
            case "d": 
                r = 3
                l = 1.25
            case "e": 
                r = 2
                l = 1
            case "f": 
                r = 1
                l = 0.75
    else:
        r = 3
        l = 1.5
        m = "d"
elif randommode == "r":
    if m in {"dev","s", "a", "b", "c", "d", "e", "f"}:
        match m:
            case "dev": 
                r = 10
                l = 10000
                standartwartezeit = 0.2
            case "sss": 
                r = 9
                l = 1000
            case "ss": 
                r = 8
                l = 100
            case "s": 
                r = 7
                l = 10
            case "a": 
                r = 6
                l = 5
            case "b": 
                r = 5
                l = 2
            case "c": 
                r = 4
                l = 1.5
            case "d": 
                r = 3
                l = 1.25
            case "e": 
                r = 2
                l = 1
            case "f": 
                r = 1
                l = 0.75

player1 = {"name": name,"alter": 0,"leben": 100*l, "rank": r}
player1 = lg.weaponsgetaddon(player1)

moa = {"name": "Der Dämonenkönig","alter": rd.randint(101,1000000),"attack-s": 90000000,"leben": 500000,"waffe": "schießt mit Atomic gegen", "rank": 20}

die = 0
dieten = 1
goblin1 = moa #goblin1 ist der letze gegen den man gespielt hat
print("")
while True:# Wiederholung Unendlich mit einigen außnahmen
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

    #addons
    f = open("verb.json")
    verblist = json.load(f)
    f = open("enemy.json")
    enemylist = json.load(f)
    f = open("locations.json")
    locationslist = json.load(f)

    # Replace characters in the JSON objects
    enemylist = lg.replace_umlauts(enemylist)
    locationslist = lg.replace_umlauts(locationslist)
    verblist = lg.replace_umlauts(verblist)


    verb = rd.choice(verblist)

    if rd.randint(1,2) == 2:
        location = rd.choice(locationslist)
        print(player1["name"] + " " + verb["verb"] + " " + location["info"])
    else:
        enemy = rd.choice(enemylist)
        bodylocationslist = ["an totem " + enemy["name"] + " vorbei","an einem " + enemy["name"] + " vorbei"] 
        bodylocation = rd.choice(bodylocationslist)
        print(player1["name"] + " " + verb["verb"] + " " + bodylocation)
    print("")
    print("")
    time.sleep(standartwartezeit)

    if rd.randint(r,20) > 10: #Kampf
                        time.sleep(standartwartezeit)
                        enemy = rd.choice(enemylist)
                        enemy["alter"] += rd.randint(0,30)
                        enemy["leben"] = enemy["leben"] * int(float(l) * float(rd.randint(80 ,120))/100)
                        enemy = lg.weaponsgetaddon(enemy)
                        enemy = lg.fight(player1,enemy,die*dieten)
                        goblin1 = enemy
                        if enemy["leben"] < 1:
                            print(enemy["name"] + " ist gestorben er war " + str(enemy["alter"]) + " Jahre alt")
                            die += 4 #die beschreibt wie oft jemand schon gestorben sind. Um später dann den Dämonenkönig auszuwählen
                            print(" ")
                            print(" ")
    if die > 0:
        if player1["leben"] > 0: #Regenerierung Player1
            if player1["leben"] < 1000000:
                if player1["leben"] > 200:player1["leben"] += 5*r
                else:player1["leben"] += 25*r
    if die > 10:
        print("Level Up")
        dieten += 1
        die -= 10
        r += 1
        if m == "f":
            m = "e"
        elif m == "e":
            m = "d"
        elif m == "d":
            m = "c"
        elif m == "c":
            m = "b"
        elif m == "b":
            m = "a"
        elif m == "a":
            m = "s"
        elif m == "s":
            m = "ss"
        elif m == "ss":
            m = "sss"
        elif m == "sss":
            print(player1["name"] + "ist jetzt auf dem maximalem Level")
            r = 10
            l = 1000000000
        if randommode != "r":
            if m in {"dev","sss","ss","s", "a", "b", "c", "d", "e", "f"}:
                match m:
                    case "dev": 
                        r = 10
                        l = 10000
                        standartwartezeit = 0.2
                    case "sss": 
                        r = 9
                        l = 1000
                    case "ss": 
                        r = 8
                        l = 100
                    case "s": 
                        r = 7
                        l = 10
                    case "a": 
                        r = 6
                        l = 5
                    case "b": 
                        r = 5
                        l = 2
                    case "c": 
                        r = 4
                        l = 1.5
                    case "d": 
                        r = 3
                        l = 1.25
                    case "e": 
                        r = 2
                        l = 1
                    case "f": 
                        r = 1
                        l = 0.75
            else:
                r = 3
                l = 1.5
                m = "d"
        elif randommode == "r":
            if m in {"dev","sss","ss","s", "a", "b", "c", "d", "e", "f"}:
                match m:
                    case "dev": 
                        r = 10
                        l = 10000
                        standartwartezeit = 0.2
                    case "sss": 
                        r = 9
                        l = 1000
                    case "ss": 
                        r = 8
                        l = 100
                    case "s": 
                        r = 7
                        l = 10
                    case "a": 
                        r = 6
                        l = 5
                    case "b": 
                        r = 5
                        l = 2
                    case "c": 
                        r = 4
                        l = 1.5
                    case "d": 
                        r = 3
                        l = 1.25
                    case "e": 
                        r = 2
                        l = 1
                    case "f": 
                        r = 1
                        l = 0.75
                
        player1 = {"name": player1["name"],"alter": player1["alter"],"attack-s": player1["attack-s"]*1.03,"leben": 100*l, "waffe": player1["waffe"], "rank": r}
        player1 = lg.weaponsgetaddon(player1)
    time.sleep(standartwartezeit)

time.sleep(10)
