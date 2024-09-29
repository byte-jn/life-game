import json
import random as rd
from replace_umlauts import replace_umlauts

def weaponsgetaddon(object1, randommode): 
    with open("weapondmg.json") as f:
        weapon_data = json.load(f)
        weaponlist = weapon_data[0]  # Access the dictionary within the list
    
    weaponlist = replace_umlauts(weaponlist)

    if randommode == "r":
        if object1["rank"] < 11:
            weapon_rank_key = f"r{rd.randint(1, 10)}"
            if weapon_rank_key in weaponlist:
                rank_weaponlist = weaponlist[weapon_rank_key]
                weapon = rd.choice(rank_weaponlist)
            else:
                raise ValueError(f"Rank {rd.randint(1, 10)} not found in weaponlist")
        else:
            weapon = {
                "name": "deatomize",
                "waffe": "deatomize",
                "attack-s": 1000000000000000000000000000
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
                    weapon_rank_key = f"r{object1['rank'] - a}"
                    if weapon_rank_key in weaponlist:
                        rank_weaponlist = rank_weaponlist + weaponlist[weapon_rank_key]
                    else: 
                        weapon_rank_key_true = False
                weapon = rd.choice(rank_weaponlist)
            else:
                raise ValueError(f"Rank {object1['rank']} not found in weaponlist")
        else:
            weapon = {
                "name": "Power of Infinity",
                "waffe": "shot with the magic of infinity",
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
