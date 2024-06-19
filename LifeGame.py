import random as rd, os, time #importieren von verschiedensten Sachen
standartwartezeit = 2 #standart wartezeit :)
class LifeGameMain:#Alle wichtigen abläufe in dieser class
        def weaponsgetdmg(y,z):#Waffe aussuchen
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
                    x = "schoß mit every gun einen Kuh auf"
            return x #Den coolen satz zurückgeben
        def fight(gegner):#Der Kampf
            if die > rd.randint(20,101):gegner = moa #zufällige Variable für den Spawn des Dämonenkönigs
            print(player1["name"] + " kämpft gegen " + gegner["name"])#Anzeige für den Kampf
            if rd.randint(1,2) == 1:xs = True #Wer fängt an? Entscheidung durch Zufall
            else: xs = False
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
            return gegner #Alle wichtigen Infos vom gegner zurück geben
print("Wie stark willst du sein? (s/a/b/c/d/e/f)?")
m = input("Stärke = ")
if m in {"ss","s", "a", "b", "c", "d", "e", "f"}:
    match m:
        case "ss": 
            n = 1
            b = 1
            l = 100
        case "s": 
            n = 1
            b = 1
            l = 10
        case "a": 
            n = 2
            b = 3
            l = 5
        case "b": 
            n = 8
            b = 4
            l = 2
        case "c": 
            n = 20
            b = 9
            l = 1.5
        case "d": 
            n = 50
            b = 20
            l = 1.25
        case "e": 
            n = 70
            b = 50
            l = 1
        case "f": 
            n = 90
            b = 70
            l = 0.75
else:
    n = 10
    b = 1
    l = 2
lg = LifeGameMain #class in eine einfache Variable packen um darauf einfach zugreifen zu können
player1 = {"name": "Harald","alter": 0,"attack-s": lg.weaponsgetdmg(n,b),"leben": 100*l}
player1 = {"name": player1["name"],"alter": player1["alter"],"attack-s": player1["attack-s"],"leben": player1["leben"],"waffe": str(lg.weaponsget(player1["attack-s"]))}
mensch = {"name": "Mensch","alter": rd.randint(25,39),"attack-s": lg.weaponsgetdmg(50,1),"leben": 100}
mensch = {"name": mensch["name"],"alter": mensch["alter"],"attack-s": mensch["attack-s"],"leben": mensch["leben"],"waffe": str(lg.weaponsget(mensch["attack-s"]))}
magier = {"name": "Magier","alter": rd.randint(50,90),"attack-s": lg.weaponsgetdmg(30,1),"leben": 130}
magier = {"name": magier["name"],"alter": magier["alter"],"attack-s": magier["attack-s"],"leben": magier["leben"],"waffe": str(lg.weaponsget(magier["attack-s"]))}
demon = {"name": "Dämon","alter": rd.randint(102,620),"attack-s": lg.weaponsgetdmg(10,1),"leben": 200,}
demon = {"name": demon["name"],"alter": demon ["alter"],"attack-s": demon["attack-s"],"leben": demon["leben"],"waffe": str(lg.weaponsget(demon["attack-s"]))}
goblin = {"name": "Goblin","alter": rd.randint(4,15),"attack-s": lg.weaponsgetdmg(70,1),"leben": 20,}
goblin = {"name": goblin["name"],"alter": goblin ["alter"],"attack-s": goblin["attack-s"],"leben": goblin["leben"],"waffe": str(lg.weaponsget(goblin["attack-s"]))}
chicken = {"name": "Huhn","alter": rd.randint(0,3),"attack-s": lg.weaponsgetdmg(100,1),"leben": 5,}
chicken = {"name": chicken["name"],"alter": chicken ["alter"],"attack-s": chicken["attack-s"],"leben": chicken["leben"],"waffe": str(lg.weaponsget(goblin["attack-s"]))}
moa = {"name": "Moa (der Dämonenkönig)","alter": rd.randint(101,1000000),"attack-s": 90000000,"leben": 500000,"waffe": "schießt mit Atomic gegen"}
die = 0
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
    goblin["alter"] += 1
    mensch["alter"] += 1
    magier["alter"] += 1

    x = rd.randint(1,15)
    match x:
        case 1:ortx = "in einem Wald"
        case 2:ortx = "in eine verlassene Stadt"
        case 3:ortx = "in eine menschenreiche Stadt"
        case 4:ortx = "in ein Dorf"
        case 5:ortx = "zu einem Strand"
        case 6:ortx = "in einen Süßigkeitenladen"
        case 7:ortx = "in den Himmel"
        case 8:ortx = "in eine Höhle"
        case 9:ortx = "in die Hölle"
        case 10:ortx = "zu einem Freund"
        case 11:
                print(player1["name"] + " läuft an totem " + goblin["name"] + " vorbei")
                print(" ")
                print(" ")
        case 12:
                print(player1["name"] + " läuft an totem " + mensch["name"] + " vorbei")
                print(" ")
                print(" ")
        case 13:
                print(player1["name"] + " läuft an totem " + magier["name"] + " vorbei")
                print(" ")
                print(" ")
        case 14:
                print(player1["name"] + " läuft an totem " + demon["name"] + " vorbei")
                print(" ")
                print(" ")
        case 15:
                print(player1["name"] + " läuft an totem " + chicken["name"] + " vorbei")
                print(" ")
                print(" ")
    print(player1["name"] + " geht " + ortx)
    print("")
    print("")
    time.sleep(standartwartezeit)

    if rd.randint(1,20) < 10:
        match rd.randint(1,5):#Zufälliges Ereignis
            case 1: #Kampf mit Goblin
                goblin = lg.fight(goblin)
                goblin1 = goblin
                if goblin["leben"] < 1:#Goblin Wiederbelebung und Verbesserung
                    print(goblin["name"] + "i st gestorben er war " + str(goblin["alter"]) + " Jahre alt")
                    g = int(float(die)  / float(5)) + 10
                    goblin = {"name": "einen Goblin","alter": rd.randint(4,15),"attack-s": lg.weaponsgetdmg(g,1),"leben": 20,}
                    goblin = {"name": goblin["name"],"alter": goblin ["alter"],"attack-s": goblin["attack-s"],"leben": goblin["leben"],"waffe": str(lg.weaponsget(goblin["attack-s"]))}
                    die += 1 #die beschreibt wie oft jemand schon gestorben sind. Um später dann den Dämonenkönig auszuwählen
                    print(" ")
                    print(" ")
            case 2: #Kampf mit Mensch
                time.sleep(standartwartezeit)
                mensch = lg.fight(mensch)
                goblin1 = mensch
                if mensch["leben"] < 1:#Mensch Wiederbelebung und Verbesserung
                    print(mensch["name"] + " ist gestorben er war " + str(mensch["alter"]) + " Jahre alt")
                    m = int(float(die)  / float(5)) + 50
                    mensch = {"name": "Mensch","alter": rd.randint(25,39),"attack-s": lg.weaponsgetdmg(m,1),"leben": 100}
                    mensch = {"name": mensch["name"],"alter": mensch["alter"],"attack-s": mensch["attack-s"],"leben": mensch["leben"],"waffe": str(lg.weaponsget(mensch["attack-s"]))}
                    die += 1 #die beschreibt wie oft jemand schon gestorben sind. Um später dann den Dämonenkönig auszuwählen
                    print(" ")
                    print(" ") 
            case 3: #Kampf mit Magier
                time.sleep(standartwartezeit)
                magier = lg.fight(magier)
                goblin1 = magier
                if magier["leben"] < 1:#Magier Wiederbelebung und Verbesserung
                    print(magier["name"] + " ist gestorben er war " + str(magier["alter"]) + " Jahre alt")
                    m = int(float(die)  / float(5)) + 70
                    magier = {"name": "Magier","alter": rd.randint(50,90),"attack-s": lg.weaponsgetdmg(m,1),"leben": 130}
                    magier = {"name": magier["name"],"alter": magier["alter"],"attack-s": magier["attack-s"],"leben": magier["leben"],"waffe": str(lg.weaponsget(magier["attack-s"]))}
                    die += 1 #die beschreibt wie oft jemand schon gestorben sind. Um später dann den Dämonenkönig auszuwählen
                    print(" ")
                    print(" ")
            case 4: #Kampf mit Demon
                time.sleep(standartwartezeit)
                demon = lg.fight(demon)
                goblin1 = demon
                if demon["leben"] < 1:#Demon Wiederbelebung und Verbesserung
                    print(demon["name"] + " ist gestorben er war " + str(demon["alter"]) + " Jahre alt")
                    d = int(float(die)  / float(5)) + 90
                    demon = {"name": "Dämon","alter": rd.randint(102,620),"attack-s": lg.weaponsgetdmg(d,1),"leben": 200,}
                    demon = {"name": demon["name"],"alter": demon ["alter"],"attack-s": demon["attack-s"],"leben": demon["leben"],"waffe": str(lg.weaponsget(demon["attack-s"]))}
                    die += 1 #die beschreibt wie oft jemand schon gestorben sind. Um später dann den Dämonenkönig auszuwählen
                    print(" ")
                    print(" ")
            case 5: #Kampf mit Huhns
                time.sleep(standartwartezeit)
                chicken = lg.fight(chicken)
                goblin1 = chicken
                if chicken["leben"] < 1:#Huhn Wiederbelebung und Verbesserung
                    print(chicken["name"] + " ist gestorben er war " + str(chicken["alter"]) + " Jahre alt")
                    c = int(float(die)  / float(5)) + 30
                    chicken = {"name": "Huhn","alter": rd.randint(0,3),"attack-s": lg.weaponsgetdmg(c,1),"leben": 5,}
                    chicken = {"name": chicken["name"],"alter": chicken ["alter"],"attack-s": chicken["attack-s"],"leben": chicken["leben"],"waffe": str(lg.weaponsget(goblin["attack-s"]))}
                    die += 1 #die beschreibt wie oft jemand schon gestorben sind. Um später dann den Dämonenkönig auszuwählen
                    print(" ")
                    print(" ")
    else: #nichts passier nur wandern
        if player1["leben"] > 0: #Regenerierung Player1
            if player1["leben"] > 200:
                if player1["leben"] > 100:player1["leben"] += 1
                else:player1["leben"] += 25
    time.sleep(standartwartezeit)

time.sleep(60)