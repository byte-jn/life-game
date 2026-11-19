# life-game

A text-based hero story generated in the terminal, with battles, weapons, enemies and locations. The game is an auto-battler: you watch what the hero does.

The project exists in two versions:

- `python/` – the original version (2024). Run `python LifeGame.py` inside the folder. New locations and enemies can be added in `enemy.json` and `locations.json`.
- `java/` – a newer rewrite (2026, in progress, formerly its own repo `life-game-java`). Entities, events, items, enchantments and difficulty levels are loaded from JSON files in `resources/data/`. Libraries (Jackson) are in `lib/`.

## Umlauts (Python version)

```
(Ae) = Ä
(ae) = ä
(Oe) = Ö
(oe) = ö
(Ue) = Ü
(ue) = ü
(sz) = ß
(Sz) = ẞ
```
