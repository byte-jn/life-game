import random as rd, time #importieren von verschiedensten Sachen

def location(verblist, enemylist, player1, locationslist, standartwartezeit):
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