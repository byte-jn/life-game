from weapons import weaponsgetaddon
import time

def levelup(die,dieten,randommode,player1,standartwartezeit,r,m,l): 
        time.sleep(standartwartezeit)
        print("Level Up")
        dieten += 1
        die -= 10
        r += 1
        print(str(player1["name"]) + " ist jetzt level " + str(r)+ ".")
        print("")
        if randommode != "r":
            if m in {"dev","ssss","sss","ss","s", "a", "b", "c", "d", "e", "f"}:
                match m:
                    case "ssss":
                        l = 1000000
                        m = "ssss"
                    case "dev": 
                        l = 10000
                        standartwartezeit = 0.2
                        print(player1["name"] + "ist jetzt auf dem maximalem Level")
                        m = "ssss"
                    case "sss": 
                        l = 1000
                        print(player1["name"] + "ist jetzt auf dem maximalem Level")
                        m = "ssss"
                    case "ss": 
                        l = 100
                        m = "sss"
                    case "s": 
                        l = 10
                        m = "ss"
                    case "a": 
                        l = 5
                        m = "s"
                    case "b": 
                        l = 2
                        m = "a"
                    case "c": 
                        l = 1.5
                        m = "b"
                    case "d": 
                        l = 1.25
                        m = "c"
                    case "e": 
                        l = 1
                        m = "d"
                    case "f": 
                        l = 0.75
                        m = "e" 
        elif randommode == "r":
            if m in {"dev","ssss","sss","ss","s", "a", "b", "c", "d", "e", "f"}:
                match m:
                    case "ssss":
                        l = 1000000
                        m = "ssss"
                    case "dev":
                        l = 1000
                        print(player1["name"] + "ist jetzt auf dem maximalem Level")
                        m = "ssss"
                    case "sss": 
                        l = 1000
                        print(player1["name"] + "ist jetzt auf dem maximalem Level")
                        m = "ssss"
                    case "ss": 
                        l = 100
                        m = "sss"
                    case "s": 
                        l = 10
                        m = "ss"
                    case "a": 
                        l = 5
                        m = "s"
                    case "b": 
                        l = 2
                        m = "a"
                    case "c": 
                        l = 1.5
                        m = "b"
                    case "d": 
                        l = 1.25
                        m = "c"
                    case "e": 
                        l = 1
                        m = "d"
                    case "f": 
                        l = 0.75
                        m = "e" 
                
        player1 = {"name": player1["name"],"alter": player1["alter"],"attack-s": player1["attack-s"]*1.03,"leben": 100*l, "waffe": player1["waffe"], "rank": r}
        player1 = weaponsgetaddon(player1,randommode)
        return die, dieten, player1, r, m, l