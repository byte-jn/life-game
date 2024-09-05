#addons
import json
from replace_umlauts import replace_umlauts

def addon():
    f = open("verb.json")
    verblist = json.load(f)
    f = open("enemy.json")
    enemylist = json.load(f)
    f = open("locations.json")
    locationslist = json.load(f)

    # Replace characters in the JSON objects
    enemylist = replace_umlauts(enemylist)
    locationslist = replace_umlauts(locationslist)
    verblist = replace_umlauts(verblist)

    return verblist, enemylist, locationslist