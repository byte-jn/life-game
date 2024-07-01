import random as rd
import time
import json
import tkinter as tk
from tkinter import messagebox

standartwartezeit = 2

class LifeGameMain:
    @staticmethod
    def weaponsgetaddon(object1):
        with open("weapondmg.json") as f:
            weapon_data = json.load(f)
            weaponlist = weapon_data[0]  # Access the dictionary within the list

        weaponlist = lg.replace_umlauts(weaponlist)

        if randommode.get() == "r":
            if object1["rank"] < 11:
                weapon_rank_key = f"r{rd.randint(1, 10)}"
                if weapon_rank_key in weaponlist:
                    rank_weaponlist = weaponlist[weapon_rank_key]
                    weapon = rd.choice(rank_weaponlist)
                else:
                    raise ValueError(f"Rank {rd.randint(1, 10)} not found in weaponlist")
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
                    while weapon_rank_key_true:
                        a += 1
                        weapon_rank_key = f"r{object1['rank'] - a}"
                        if weapon_rank_key in weaponlist:
                            rank_weaponlist += weaponlist[weapon_rank_key]
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

        object1.update({
            "attack-s": weapon["attack-s"],
            "waffe": weapon["waffe"]
        })

        return object1

    @staticmethod
    def fight(player1, gegner, die, a):
        automode = a
        if die > rd.randint(30, 301):
            moa = {"name": "Der Dämonenkönig","alter": rd.randint(101,1000000),"attack-s": 90000000,"leben": 500000,"waffe": "schießt mit Atomic gegen", "rank": 10}
            gegner = moa  # zufällige Variable für den Spawn des Dämonenkönigs
            fight_log.insert(tk.END, f"{player1['name']} kämpft gegen {gegner['name']}\n")
            fight_log.insert(tk.END, "Gegner hat sich als Dämonenkönig entpupt\n")
        else:
            if automode == "e":
                fight_log.insert(tk.END, f"Willst du gegen {gegner['name']} kämpfen?\n")
            else:
                fight_log.insert(tk.END, f"{player1['name']} kämpft gegen {gegner['name']}\n")

        xs = rd.randint(1, 2) == 1

        if automode == "e":
            fight_log.insert(tk.END, "Anfeuern gibt dem Helden 2% mehr Schaden, aber der Gegner fängt an.\n")
            fight_log.insert(tk.END, "Hinweisen lässt den Helden anfangen, aber der Gegner macht mehr Schaden.\n")
            fight_log.insert(tk.END, "Fliehen (f/n) / Kämpfen (k/j) / Hinweisen (h) / Anfeuern (a) / Waffentausch (w)\n")
            f = input()
            if f == "f" or f == "n":
                fight_log.insert(tk.END, f"{player1['name']} flieht vor {gegner['name']}\n")
                return gegner
            elif f == "h":
                player1["attack-s"] /= 1.2
                xs = True
            elif f == "w":
                player1 = lg.weaponsgetaddon(player1)
                fight_log.insert(tk.END, f"{player1['name']} hat jetzt eine neue Waffe\n")
            elif f == "a":
                player1["attack-s"] *= 1.2
                xs = False

        time.sleep(standartwartezeit)
        loopcount = 1
        loop = 0
        while True:
            loop += 1
            if gegner["leben"] < 1:
                fight_log.insert(tk.END, f"{player1['name']} hat gegen {gegner['name']} gewonnen\n")
                break
            elif player1["leben"] < 1:
                fight_log.insert(tk.END, f"{player1['name']} hat gegen {gegner['name']} verloren\n")
                break
            fight_log.insert(tk.END, f"({player1['name']}-HP: {player1['leben']} / {gegner['name']}-HP: {gegner['leben']})\n")

            if loop >= 10:
                time.sleep(standartwartezeit)
            if xs:
                if loop >= 6:
                    loopcount *= 2
                dmg = int(float(player1["attack-s"]) * (float(rd.randint(80, 120)) / 100) * loopcount)
                gegner["leben"] -= dmg
                fight_log.insert(tk.END, f"{player1['name']} {player1['waffe']} {gegner['name']}. Und macht {dmg} Schaden\n")
                xs = False
            else:
                dmg = int(float(gegner["attack-s"]) * (float(rd.randint(80, 120)) / 100) * (float(loopcount) / 1000))
                player1["leben"] -= dmg
                fight_log.insert(tk.END, f"{gegner['name']} {gegner['waffe']} {player1['name']}. Und macht {dmg} Schaden\n")
                xs = True
        if automode == "e":
            if f == "a":
                player1["attack-s"] /= 1.2
            elif f == "h":
                player1["attack-s"] *= 1.2
        return gegner

    @staticmethod
    def replace_umlauts(data):
        if isinstance(data, str):
            return (data.replace("(Ae)", "Ä")
                        .replace("(ae)", "ä")
                        .replace("(Oe)", "Ö")
                        .replace("(oe)", "ö")
                        .replace("(Ue)", "Ü")
                        .replace("(ue)", "ü")
                        .replace("(sz)", "ß"))
        elif isinstance(data, dict):
            return {key: lg.replace_umlauts(value) for key, value in data.items()}
        elif isinstance(data, list):
            return [lg.replace_umlauts(item) for item in data]
        return data

lg = LifeGameMain

def main():
    name_val = name.get()
    strength_val = strength_entry.get()
    auto_val = automode.get()
    random_val = randommode.get()

    if random_val != "r":
        if strength_val in {"dev", "sss", "ss", "s", "a", "b", "c", "d", "e", "f"}:
            r, l = strength_mapping[strength_val]
        else:
            r, l = 3, 1.5
            strength_val = "d"
    else:
        if strength_val in {"dev", "s", "a", "b", "c", "d", "e", "f"}:
            r, l = strength_mapping[strength_val]
        else:
            r, l = 3, 1.5
            strength_val = "d"

    player1 = {"name": name_val, "alter": 16, "leben": 100 * l, "rank": r}
    player1 = lg.weaponsgetaddon(player1)

    moa = {"name": "Der Dämonenkönig", "alter": rd.randint(101, 1000000), "attack-s": 90000000, "leben": 500000, "waffe": "schießt mit Atomic gegen", "rank": 10}

    die, dieten = 0, 1
    goblin1 = moa
    fight_log.insert(tk.END, f"Spiel gestartet mit Spieler: {player1['name']}\n")

    while True:
        if goblin1["leben"] < 1 and goblin1["name"] == moa["name"]:
            fight_log.insert(tk.END, f"{player1['name']} hat gegen den {goblin1['name']} gewonnen\n")
            fight_log.insert(tk.END, "Warte. Was!? Wie!?\n")
            time.sleep(standartwartezeit)
            fight_log.insert(tk.END, "Auf Jeden Fall ist die Welt jetzt befreit\n")
            fight_log.insert(tk.END, "Vielen Dank\n")
            break
        if player1["leben"] < 1:
            fight_log.insert(tk.END, f"Nach {dieten} gegnern hat {player1['name']} verloren\n")
            break
        die = rd.randint(0, 301)
        goblin1 = {"name": f"Gegner-{dieten}", "alter": rd.randint(5, 71), "leben": 40 * l, "rank": r}
        goblin1 = lg.weaponsgetaddon(goblin1)
        goblin1 = lg.fight(player1, goblin1, die, auto_val)
        dieten += 1

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()

root = tk.Tk()
root.title("Lebensspiel")

strength_mapping = {
    "dev": (15, 200),
    "sss": (10, 75),
    "ss": (8, 45),
    "s": (6, 25),
    "a": (5, 15),
    "b": (4, 7),
    "c": (3, 2.5),
    "d": (3, 1.5),
    "e": (2, 1.3),
    "f": (1, 1)
}

tk.Label(root, text="Name:").grid(row=0, column=0)
name = tk.Entry(root)
name.grid(row=0, column=1)

tk.Label(root, text="Stärke:").grid(row=1, column=0)
strength_entry = tk.Entry(root)
strength_entry.grid(row=1, column=1)

tk.Label(root, text="Auto (a)/ Manual (e):").grid(row=2, column=0)
automode = tk.Entry(root)
automode.grid(row=2, column=1)

tk.Label(root, text="Random mode (r):").grid(row=3, column=0)
randommode = tk.Entry(root)
randommode.grid(row=3, column=1)

start_button = tk.Button(root, text="Start", command=main)
start_button.grid(row=4, columnspan=2)

fight_log = tk.Text(root, height=15, width=50)
fight_log.grid(row=5, columnspan=2)

root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()
