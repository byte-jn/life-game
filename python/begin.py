from weapons import weaponsgetaddon # importing various things

def begin(standartwartezeit):
    print("Enter a name... ")
    name = input()
    print(" ")

    print("How strong do you want to be? (s/a/b/c/d/e/f)?")
    m = input("Strength = ")

    print("")
    print("Automode allows you to fight automatically without choosing what you want to do.")
    print("With input, you can choose whether you want to flee or fight and more.")
    print("Automode (a) / Input (i)...")
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
                    r = 11
                    l = 10000
                    standartwartezeit = 0.2
                    m = "ssss"
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
                    r = 11
                    l = 10000
                    standartwartezeit = 0.2
                    m = "ssss"
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
    player1 = weaponsgetaddon(player1, randommode)


    die = 0
    dieten = 1
    print("")
    return player1, die, dieten, r, l, m, automode, randommode, standartwartezeit