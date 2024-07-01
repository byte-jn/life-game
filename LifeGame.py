import random as rd
import time
import json
import pygame

# Initialisiere pygame
pygame.init()

# Setze Fenstergröße und Farben
SCREEN_WIDTH = 1024  # Neue Breite
SCREEN_HEIGHT = 768  # Neue Höhe
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Life Game")

# Schriftart und Größe
font = pygame.font.SysFont(None, 36)

# Globale Variablen
standartwartezeit = 2

class LifeGameMain:
    def weaponsgetaddon(self, object1):
        with open("weapondmg.json") as f:
            weapon_data = json.load(f)
            weaponlist = weapon_data[0]  # Access the dictionary within the list
        
        weaponlist = self.replace_umlauts(weaponlist)

        # Sicherstellen, dass der 'rank'-Schlüssel existiert
        if 'rank' not in object1:
            raise KeyError("Der Schlüssel 'rank' fehlt im übergebenen Objekt")

        if object1["rank"] < 11:
                weapon_rank_key = f"r{object1['rank']}"
                if weapon_rank_key in weaponlist:
                    rank_weaponlist = weaponlist[weapon_rank_key]
                    weapon_rank_key_true = True
                    a = 0
                    while weapon_rank_key_true:
                        a += 1
                        weapon_rank_key = f"r{object1['rank']-a}"
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
                    "waffe": "schießt mit der Magie der Unendlichkeit",
                    "attack-s": 1000000000000
                }

        object1 = {
            "name": object1.get("name", "Unbekannt"),
            "alter": object1.get("alter", 0),
            "attack-s": weapon["attack-s"],
            "leben": object1.get("leben", 100),
            "waffe": weapon["waffe"],
            "rank": object1["rank"]
        }
        
        return object1

    def fight(self, player1, gegner, die, r):
        messages = []

        if die > rd.randint(30, 301):
            moa = {"name": "Der Dämonenkönig", "alter": rd.randint(101,1000000), "attack-s": 90000000, "leben": 500000, "waffe": "schießt mit Atomic gegen", "rank": 10}
            gegner = moa
            messages.append(f"{player1['name']} kämpft gegen {gegner['name']}")
            messages.append("Gegner hat sich als Dämonenkönig entpuppt")
        else:
            messages.append(f"{player1['name']} kämpft gegen {gegner['name']}")

        xs = rd.randint(1, 2) == 1
        loopcount = 1
        loop = 0
        while True:
            loop += 1
            if gegner["leben"] < 1:
                messages.append(f"{player1['name']} hat gegen {gegner['name']} gewonnen")
                break
            elif player1["leben"] < 1:
                messages.append(f"{player1['name']} hat gegen {gegner['name']} verloren")
                break

            if loop < 10:
                time.sleep(standartwartezeit)

            if xs:
                if loop >= 6:
                    loopcount *= 2
                dmg = int(player1["attack-s"] * (rd.randint(80, 120) / 100) * loopcount)
                gegner["leben"] -= dmg
                messages.append(f"{player1['name']} {player1['waffe']} {gegner['name']}. Und macht {dmg} Schaden")
                xs = False
            else:
                dmg = int(gegner["attack-s"] * (rd.randint(80, 120) / 100) * (loopcount / 1000))
                player1["leben"] -= dmg
                messages.append(f"{gegner['name']} {gegner['waffe']} {player1['name']}. Und macht {dmg} Schaden")
                xs = True

        return gegner, messages

    def replace_umlauts(self, data):
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
                data[key] = self.replace_umlauts(value)
        elif isinstance(data, list):
            for i in range(len(data)):
                data[i] = self.replace_umlauts(data[i])
        return data

def draw_text(surface, text, position, color=BLACK):
    textobj = font.render(text, True, color)
    textrect = textobj.get_rect()
    textrect.center = position
    surface.blit(textobj, textrect)

def draw_multiple_texts(surface, texts, start_position, color=BLACK):
    y_offset = 0
    for text in texts:
        draw_text(surface, text, (surface.get_width() // 2, start_position + y_offset), color)
        y_offset += 40  # Abstand zwischen den Zeilen

def main_game():
    global standartwartezeit
    global automode
    global randommode
    global SCREEN_WIDTH
    global SCREEN_HEIGHT
    global screen

    # Initialisiere Variablen
    r = 5  # Beispielwert, setze den initialen Rang
    l = 1.5  # Beispielwert, setze den initialen Lebenswert
    name = "Held"  # Beispielname für den Spieler
    player1 = {"name": name, "alter": 0, "leben": 100 * l, "rank": r}

    lg = LifeGameMain()
    player1 = lg.weaponsgetaddon(player1)

    moa = {"name": "Der Dämonenkönig", "alter": rd.randint(101, 1000000), "attack-s": 90000000, "leben": 500000, "waffe": "schießt mit Atomic gegen", "rank": 10}

    die = 0
    goblin1 = moa

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.VIDEORESIZE:
                SCREEN_WIDTH, SCREEN_HEIGHT = event.size
                screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.RESIZABLE)

        screen.fill(WHITE)
        draw_text(screen, "Drücke ESC zum Beenden", (SCREEN_WIDTH // 2, SCREEN_HEIGHT - 20))

        if goblin1["leben"] < 1 and goblin1["name"] == moa["name"]:
            screen.fill(WHITE)  # Bildschirm löschen
            draw_text(screen, f"{player1['name']} hat gegen den {goblin1['name']} gewonnen", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
            pygame.display.flip()
            time.sleep(standartwartezeit)
            running = False
            continue  # Weiter zur nächsten Schleife

        
        #addons
        f = open("verb.json")
        verblist = json.load(f)
        f = open("enemy.json")
        enemylist = json.load(f)
        f = open("locations.json")
        locationslist = json.load(f)

        # Replace characters in the JSON objects
        enemy_list = lg.replace_umlauts(enemylist)
        locations_list = lg.replace_umlauts(locationslist)
        verb_list = lg.replace_umlauts(verblist)

        verb = rd.choice(verb_list)
        location = rd.choice(locations_list)
        screen.fill(WHITE)
        draw_text(screen, f"{player1['name']} {verb['verb']} {location['info']}", (SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        pygame.display.flip()
        time.sleep(standartwartezeit)

        if rd.randint(r, 25) > 15:
            if rd.randint(1, 5) != 1:
                enemy = rd.choice(enemy_list)
                enemy_data, messages = lg.weaponsgetaddon(enemy), []
                goblin1, messages = lg.fight(player1, enemy_data, die, r)
                die = r
                for msg in messages:
                    screen.fill(WHITE)  # Bildschirm löschen
                    draw_multiple_texts(screen, [msg], SCREEN_HEIGHT // 2 - 100)
                    pygame.display.flip()
                    time.sleep(standartwartezeit)

    pygame.quit()

if __name__ == "__main__":
    main_game()
