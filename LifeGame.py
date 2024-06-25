import random as rd, time #importieren von verschiedensten Sachen
import json

standartwartezeit = 2 #standart wartezeit :)
class LifeGameMain:#Alle wichtigen abläufe in dieser class
        def weaponsgetdmg(y,z):#Waffe aussuchen
            if y == -100:
                return 1000000000 #Schaden Sonne zurückgeben
            if z < 1: z = 1 #Aufpassen das es nicht zu niedrig ist
            if y < 1: y = 1 #Aufpassen das es nicht zu niedrig ist
            if y > z: 
                x = y
                y = z
                z = x 
            xr = rd.randint(y,z)
            if xr < 10:#Zufall
                match xr:
                    case 8:#Holzschwert
                        x = 10
                    case 1:#Every Gun 
                        x = 30
                        y = rd.randint(1,90)   
                        if y > 59:#ein Baum 150Kg
                            z = x*150
                        elif y > 39:#ein Auto 1,4 Tonnen
                            z = x*1400
                        elif y > 19:#eine Kuh 600-700kg
                            z = x*650
                        elif y > 14:#ein Haus 10000 Tonnen
                            z = x*10000
                        elif y > 9:#ein Meteorit 250kg
                            z = x*250
                        elif y > 4:#ein U-boot 26.000 Tonnen
                            z = x*26000
                        elif y > 1:#ein Schiff 100.000 Tonnen
                            z = x*100000
                        elif y == 1:#der Mond 7*10^6 Tonnen
                            z = x*7000000
                        else:#einen kleiner Stein 1 Kg
                            z = x*1                  
                        x = z
                    case 4:#Barett m90
                        x = 200
                    case 9:#Stock
                        x = 5
                    case 7:#Bogen Holz
                        x = 20
                    case 6:#Bogen Stahl
                        x = 50
                    case 5:#Plasma Pistole
                        x = 60
                    case 2:#Panzer
                        x = 760
                    case 3:#Beam Canon
                        x = 220    
            else: #Hand
                x = 1
            return x #Schaden zurückgeben
        def weaponsget(x):#Waffenspruch aussuchen
            match x:#Waffespruch nach schaden suchen der zuvor ausgesucht worde
                case 1:#Hand
                    x = "schlägt mit der Hand auf"
                case 5:#Stock
                    x = "schlägt mit einem Stock auf" 
                case 10:#Holzscwert
                    x = "schlug mit einem Schwert gegen"
                case 20:#Bogen
                    x = "schoß mit einem Bogen auf"
                case 50:#Bogen Stahl
                    x = "schoß mit einem Stahl bogen auf"
                case 60:#Plasma Pistole
                    x = "schoß mit einer Plasma Pistole auf"
                case 200:#Barett m90
                    x = "schoß mit einem Barett m90 auf"
                case 220:#beam canon
                    x = "schoß mit einer beam canon auf"
                case 760:#Panzer
                    x = "schoß einem Panzerkugel auf"
                case 30:#Every Gun #einen kleiner Stein 1 Kg
                    x = "schoß mit every gun einen Stein auf"
                case 300000:#Every Gun #ein Haus 100 Tonnen
                    x = "schoß mit every gun ein Haus auf"
                case 3000000:#Every Gun #ein Schiff 100.000 Tonnen
                    x = "schoß mit every gun ein Schiff auf"
                case 4500:#Every Gun #ein Baum 150Kg
                    x = "schoß mit every gun einen Baum auf"
                case 780000:#Every Gun #ein U-boot 26.000 Tonnen
                    x = "schoß mit every gun ein U-Boot auf"
                case 210000000:#Every Gun #der Mond 7*10^19 Tonnen
                    x = "schoß mit every gun einen Mond auf"
                case 7500:#Every Gun #ein Meteorit 250kg
                    x = "schoß mit every gun einen Mond auf"
                case 42000:#Every Gun #ein Auto 1,4 Tonnen
                    x = "schoß mit every gun ein Auto auf"
                case 19500:#Every Gun #eine Kuh 600-700kg
                    x = "warf einen Kuh auf"
                case 1000000000:
                    x = "warf die Sonne auf"
            return x #Den coolen satz zurückgeben
        def fight(automode,n,b,player1,gegner,die):#Der Kampf
            if die > rd.randint(30,301):
                gegner = moa #zufällige Variable für den Spawn des Dämonenkönigs
                print("Gegner hat sich als Dämonenkönig entpupt")
            print(player1["name"] + " kämpft gegen " + gegner["name"])#Anzeige für den Kampf
            if rd.randint(1,2) == 1:xs = True #Wer fängt an? Entscheidung durch Zufall
            else: xs = False
            if automode == "a":
                print("")
                print("")
                time.sleep(2)
                print("Anfeuern gibt dem Helden 2% mehr schaden, aber der Gegner fängt an")
                print("Hinweisen lässt den Helden an fangen, aber der Gegner macht mehr schaden")
                print("")
                print("fliehen (f) / kämpfen (k) / hinweisen (h) / anfeuern (a) / Waffetausch (w)")
                f = input()
                print("")
                if f == "f": 
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
                    player1["attack-s"] = lg.weaponsgetdmg(n,b)
                    player1["waffe"] = lg.weaponsget(player1["attack-s"])
                    print(player1["name"] + " hat jetzt eine neue Waffe")
                    print("")
                elif f == "a": 
                    player1["attack-s"] = player1["attack-s"] * 1.2
                print("")
            if die < 1: xs = True
            while True:#Loop bis Jemand tod ist
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
                    dmg = int(float(player1["attack-s"])*(float(rd.randint(50,150))/float(100)))
                    gegner["leben"] = gegner["leben"] - dmg
                    print( player1["name"] + " " + player1["waffe"] + " " + gegner["name"] + ". Und macht " + str(dmg) + " Schaden")
                    xs = False
                else:#Gegner schlägt zu
                    dmg = int(float(gegner["attack-s"])*(float(rd.randint(50,150))/float(100)))
                    player1["leben"] = player1["leben"] - dmg
                    print( gegner["name"] + " " + gegner["waffe"] + " " + player1["name"] + ". Und macht " + str(dmg) + " Schaden")
                    xs = True
            if automode == "a":
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
if m in {"dev","s", "a", "b", "c", "d", "e", "f"}:
    match m:
        case "dev": 
            r = 10
            n = 1
            b = 1
            l = 1000
            standartwartezeit = 0.2
        case "s": 
            r = 7
            n = 1
            b = 5
            l = 10
        case "a": 
            r = 6
            n = 2
            b = 6
            l = 5
        case "b": 
            r = 5
            n = 4
            b = 7
            l = 2
        case "c": 
            r = 4
            n = 5
            b = 10
            l = 1.5
        case "d": 
            r = 3
            n = 6
            b = 12
            l = 1.25
        case "e": 
            r = 2
            n = 7
            b = 15
            l = 1
        case "f": 
            r = 1
            n = 9
            b = 17
            l = 0.75
else:
    r = 3
    n = 20
    b = 1
    l = 2
    m = "d"
print("")
print("Automode lässt dich automatisch kämpfen und nicht auswählen was du machen willst.")
print("Bei Eingabe kannst du auswählen ob du fliehen willst oder kämpfen möchtest und mehr.")
print("Automode (a) / Eingabe (e)...")
automode = input("Mode = ")

player1 = {"name": name,"alter": 0,"attack-s": lg.weaponsgetdmg(n,b),"leben": 200*l}
player1 = {"name": player1["name"],"alter": player1["alter"],"attack-s": player1["attack-s"],"leben": player1["leben"],"waffe": str(lg.weaponsget(player1["attack-s"]))}
mensch = {"name": "Mensch","alter": rd.randint(25,39),"attack-s": lg.weaponsgetdmg(10,2),"leben": 100}
mensch = {"name": mensch["name"],"alter": mensch["alter"],"attack-s": mensch["attack-s"],"leben": mensch["leben"],"waffe": str(lg.weaponsget(mensch["attack-s"]))}
magier = {"name": "Magier","alter": rd.randint(50,90),"attack-s": lg.weaponsgetdmg(6,2),"leben": 130}
magier = {"name": magier["name"],"alter": magier["alter"],"attack-s": magier["attack-s"],"leben": magier["leben"],"waffe": str(lg.weaponsget(magier["attack-s"]))}
demon = {"name": "Dämon","alter": rd.randint(102,620),"attack-s": lg.weaponsgetdmg(5,2),"leben": 200,}
demon = {"name": demon["name"],"alter": demon ["alter"],"attack-s": demon["attack-s"],"leben": demon["leben"],"waffe": str(lg.weaponsget(demon["attack-s"]))}
goblin = {"name": "Goblin","alter": rd.randint(4,15),"attack-s": lg.weaponsgetdmg(20,7),"leben": 20,}
goblin = {"name": goblin["name"],"alter": goblin ["alter"],"attack-s": goblin["attack-s"],"leben": goblin["leben"],"waffe": str(lg.weaponsget(goblin["attack-s"]))}
chicken = {"name": "Huhn","alter": rd.randint(1,4),"attack-s": lg.weaponsgetdmg(15,9),"leben": 5,}
chicken = {"name": chicken["name"],"alter": chicken ["alter"],"attack-s": chicken["attack-s"],"leben": chicken["leben"],"waffe": str(lg.weaponsget(chicken["attack-s"]))}
moa = {"name": "Moa (der Dämonenkönig)","alter": rd.randint(101,1000000),"attack-s": 90000000,"leben": 500000,"waffe": "schießt mit Atomic gegen"}

die = 0
dieten = 1
goblin1 = goblin #goblin1 ist der letze gegen den man gespielt hat
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


    verb = [" geht", " läuft", " springt", " wandert", " sprintet", " läuft vorsichtig", " fliegt", " geht erneut", " taucht", " klettert", " gräbt sich", " bohrt sich", " fällt", " kackt", ""]

    #addons
    f = open("enemy.json")
    enemylist = json.load(f)
    f = open("locations.json")
    locationslist = json.load(f)

    # Replace characters in the JSON objects
    enemylist = lg.replace_umlauts(enemylist)
    locationslist = lg.replace_umlauts(locationslist)

    if rd.randint(1,2) == 2:
        location = rd.choice(locationslist)
        verb = rd.choice(verb)
        print(player1["name"] + verb + location["info"])
    else:
        enemy = rd.choice(enemylist)
        verb = rd.choice(verb)
        bodylocationslist = [" an totem " + enemy["name"] + " vorbei", " an totem " + goblin["name"] + " vorbei", " an totem " + mensch["name"] + " vorbei", " an totem " + magier["name"] + " vorbei", " an totem " + demon["name"] + " vorbei", " an totem " + chicken["name"] + " vorbei", " an einem " + enemy["name"] + " vorbei", " an einem " + goblin["name"] + " vorbei", " an einem " + mensch["name"] + " vorbei", " an einem " + magier["name"] + " vorbei", " an einem " + demon["name"] + " vorbei", " an einem " + chicken["name"] + " vorbei"] 
        bodylocation = rd.choice(bodylocationslist)
        print(player1["name"] + verb + bodylocation)
    print("")
    print("")
    time.sleep(standartwartezeit)

    if rd.randint(r,12) > 10:
        if r < 2:#Kampf mit Huhns
                            time.sleep(standartwartezeit)
                            chicken = lg.fight(automode,n,b,player1,chicken,die*dieten)
                            goblin1 = chicken
                            if chicken["leben"] < 1:#Huhn Wiederbelebung und Verbesserung
                                print(chicken["name"] + " ist gestorben er war " + str(chicken["alter"]) + " Jahre alt")
                                die += 1 #die beschreibt wie oft jemand schon gestorben sind. Um später dann den Dämonenkönig auszuwählen
                                chicken = {"name": "Huhn","alter": rd.randint(1,4),"attack-s": lg.weaponsgetdmg(15,9),"leben": 5,}
                                chicken = {"name": chicken["name"],"alter": chicken ["alter"],"attack-s": chicken["attack-s"],"leben": chicken["leben"],"waffe": str(lg.weaponsget(chicken["attack-s"]))}
                                print(" ")
                                print(" ")
        else:
            if r < 4:
                match rd.randint(1,2):#Zufälliges Ereignis
                        case 1: #Kampf mit Goblin
                            time.sleep(standartwartezeit)
                            goblin = lg.fight(automode,n,b,player1,goblin,die*dieten)
                            goblin1 = goblin
                            if goblin["leben"] < 1:#Goblin Wiederbelebung und Verbesserung
                                print(goblin["name"] + " ist gestorben er war " + str(goblin["alter"]) + " Jahre alt")
                                die += 2 #die beschreibt wie oft jemand schon gestorben sind. Um später dann den Dämonenkönig auszuwählen
                                goblin = {"name": "Goblin","alter": rd.randint(4,15),"attack-s": lg.weaponsgetdmg(20,7),"leben": 20,}
                                goblin = {"name": goblin["name"],"alter": goblin ["alter"],"attack-s": goblin["attack-s"],"leben": goblin["leben"],"waffe": str(lg.weaponsget(goblin["attack-s"]))}
                                print(" ")
                                print(" ")
                        case 5: #Kampf mit Huhns
                            time.sleep(standartwartezeit)
                            chicken = lg.fight(automode,n,b,player1,chicken,die*dieten)
                            goblin1 = chicken
                            if chicken["leben"] < 1:#Huhn Wiederbelebung und Verbesserung
                                print(chicken["name"] + " ist gestorben er war " + str(chicken["alter"]) + " Jahre alt")
                                die += 1 #die beschreibt wie oft jemand schon gestorben sind. Um später dann den Dämonenkönig auszuwählen
                                chicken = {"name": "Huhn","alter": rd.randint(1,4),"attack-s": lg.weaponsgetdmg(15,9),"leben": 5,}
                                chicken = {"name": chicken["name"],"alter": chicken ["alter"],"attack-s": chicken["attack-s"],"leben": chicken["leben"],"waffe": str(lg.weaponsget(chicken["attack-s"]))}
                                print(" ")
                                print(" ")
            else:
                if rd.randint(1,5) != 2:
                    match rd.randint(1,5):#Zufälliges Ereignis
                        case 1: #Kampf mit Goblin
                            time.sleep(standartwartezeit)
                            goblin = lg.fight(automode,n,b,player1,goblin,die*dieten)
                            goblin1 = goblin
                            if goblin["leben"] < 1:#Goblin Wiederbelebung und Verbesserung
                                print(goblin["name"] + " ist gestorben er war " + str(goblin["alter"]) + " Jahre alt")
                                die += 1 #die beschreibt wie oft jemand schon gestorben sind. Um später dann den Dämonenkönig auszuwählen
                                goblin = {"name": "Goblin","alter": rd.randint(4,15),"attack-s": lg.weaponsgetdmg(20,7),"leben": 20,}
                                goblin = {"name": goblin["name"],"alter": goblin ["alter"],"attack-s": goblin["attack-s"],"leben": goblin["leben"],"waffe": str(lg.weaponsget(goblin["attack-s"]))}
                                print(" ")
                                print(" ")
                        case 2: #Kampf mit Mensch
                            time.sleep(standartwartezeit)
                            mensch = lg.fight(automode,n,b,player1,mensch,die*dieten)
                            goblin1 = mensch
                            if mensch["leben"] < 1:#Mensch Wiederbelebung und Verbesserung
                                print(mensch["name"] + " ist gestorben er war " + str(mensch["alter"]) + " Jahre alt")
                                die += 3 #die beschreibt wie oft jemand schon gestorben sind. Um später dann den Dämonenkönig auszuwählen
                                mensch = {"name": "Mensch","alter": rd.randint(25,39),"attack-s": lg.weaponsgetdmg(10,2),"leben": 100}
                                mensch = {"name": mensch["name"],"alter": mensch["alter"],"attack-s": mensch["attack-s"],"leben": mensch["leben"],"waffe": str(lg.weaponsget(mensch["attack-s"]))}
                                print(" ")
                                print(" ") 
                        case 3: #Kampf mit Magier
                            time.sleep(standartwartezeit)
                            magier = lg.fight(automode,n,b,player1,magier,die*dieten)
                            goblin1 = magier
                            if magier["leben"] < 1:#Magier Wiederbelebung und Verbesserung
                                print(magier["name"] + " ist gestorben er war " + str(magier["alter"]) + " Jahre alt")
                                die += 3 #die beschreibt wie oft jemand schon gestorben sind. Um später dann den Dämonenkönig auszuwählen
                                magier = {"name": "Magier","alter": rd.randint(50,90),"attack-s": lg.weaponsgetdmg(6,2),"leben": 130}
                                magier = {"name": magier["name"],"alter": magier["alter"],"attack-s": magier["attack-s"],"leben": magier["leben"],"waffe": str(lg.weaponsget(magier["attack-s"]))}
                                print(" ")
                                print(" ")
                        case 4: #Kampf mit Demon
                            time.sleep(standartwartezeit)
                            demon = lg.fight(automode,n,b,player1,demon,die*dieten)
                            goblin1 = demon
                            if demon["leben"] < 4:#Demon Wiederbelebung und Verbesserung
                                print(demon["name"] + " ist gestorben er war " + str(demon["alter"]) + " Jahre alt")
                                die += 1 #die beschreibt wie oft jemand schon gestorben sind. Um später dann den Dämonenkönig auszuwählen
                                demon = {"name": "Dämon","alter": rd.randint(102,620),"attack-s": lg.weaponsgetdmg(5,2),"leben": 200,}
                                demon = {"name": demon["name"],"alter": demon ["alter"],"attack-s": demon["attack-s"],"leben": demon["leben"],"waffe": str(lg.weaponsget(demon["attack-s"]))}
                                print(" ")
                                print(" ")
                        case 5: #Kampf mit Huhns
                            time.sleep(standartwartezeit)
                            chicken = lg.fight(automode,n,b,player1,chicken,die*dieten)
                            goblin1 = chicken
                            if chicken["leben"] < 1:#Huhn Wiederbelebung und Verbesserung
                                print(chicken["name"] + " ist gestorben er war " + str(chicken["alter"]) + " Jahre alt")
                                die += 1 #die beschreibt wie oft jemand schon gestorben sind. Um später dann den Dämonenkönig auszuwählen
                                chicken = {"name": "Huhn","alter": rd.randint(1,4),"attack-s": lg.weaponsgetdmg(15,9),"leben": 5,}
                                chicken = {"name": chicken["name"],"alter": chicken ["alter"],"attack-s": chicken["attack-s"],"leben": chicken["leben"],"waffe": str(lg.weaponsget(chicken["attack-s"]))}
                                print(" ")
                                print(" ")
                else: #Random Kampf
                        time.sleep(standartwartezeit)
                        enemy = rd.choice(enemylist)
                        enemy["alter"] = rd.randint(5,150)
                        enemy = lg.fight(automode,n,b,player1,enemy,die*dieten)
                        goblin1 = enemy
                        if enemy["leben"] < 1:
                            print(enemy["name"] + " ist gestorben er war " + str(enemy["alter"]) + " Jahre alt")
                            die += 4 #die beschreibt wie oft jemand schon gestorben sind. Um später dann den Dämonenkönig auszuwählen
                            print(" ")
                            print(" ")
    if die > 0:
        if player1["leben"] > 0: #Regenerierung Player1
            if player1["leben"] < 1000:
                if player1["leben"] > 200:player1["leben"] += 5
                else:player1["leben"] += 25
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
            n = -100
            b = -100
            l = 1000000
        else:
            match m:
                    case "sss": 
                        r = 9
                        n = 1
                        b = 1
                        l = 1000
                    case "ss": 
                        r = 8
                        n = 1
                        b = 1
                        l = 100
                    case "s": 
                        r = 7
                        n = 1
                        b = 5
                        l = 10
                    case "a": 
                        r = 6
                        n = 2
                        b = 7
                        l = 5
                    case "b": 
                        r = 5
                        n = 4
                        b = 7
                        l = 2
                    case "c": 
                        r = 4
                        n = 5
                        b = 10
                        l = 1.5
                    case "d": 
                        r = 3
                        n = 7
                        b = 12
                        l = 1.25
                    case "e": 
                        r = 2
                        n = 8
                        b = 15
                        l = 1
                    case "f": 
                        r = 1
                        n = 10
                        b = 19
                        l = 0.75
        
        player1 = {"name": player1["name"],"alter": player1["alter"],"attack-s": lg.weaponsgetdmg(n,b),"leben": player1["leben"]*l}
        player1 = {"name": player1["name"],"alter": player1["alter"],"attack-s": player1["attack-s"],"leben": player1["leben"],"waffe": str(lg.weaponsget(player1["attack-s"]))}
    time.sleep(standartwartezeit)

time.sleep(10)
