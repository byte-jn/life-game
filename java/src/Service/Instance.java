package Service;

import Entitys.*;

import java.util.List;
import java.util.concurrent.ThreadLocalRandom;

import static Service.MinorFunction.*;

public class Instance {
    private final List<MobEntity> mobs;
    private final List<Weapon> weapons;
    private final List<Enchantment> enchantments;
    private final List<Item> items;
    private final List<Info> infos;
    private final List<Location> locations;
    private final List<Event> events;
    private final List<Player> players;
    private Player player;

    public Instance() throws Exception {
        mobs = EntityRepository.getMobEntities();
        weapons = EntityRepository.getWeapons();
        enchantments = EntityRepository.getEnchantments();
        items = EntityRepository.getItems();
        infos = EntityRepository.getInfos();
        locations = EntityRepository.getLocations();
        events = EntityRepository.getEvents();
        players = EntityRepository.getPlayers();
        player = null;
    }

    /**
     * Prints All Entities in detail
     */
    public void printAllEntities() {
        System.out.println("Entities.Mobs:");
        for (MobEntity mob : mobs) {
            System.out.println("  Name: " + mob.getName());
            System.out.println("    Health: " + mob.health);
            System.out.println("    Max Health: " + mob.getMaxHealth());
            System.out.println("    Regeneration Rate: " + mob.getRegenerationRate());
            System.out.println("-----------------------------------");
        }
        System.out.println("Weapons:");
        for (Weapon weapon : weapons) {
            System.out.println("  Name: " + weapon.getName());
            System.out.println("    Count: " + weapon.getCount());
            System.out.println("    Damage: " + weapon.getDamage());
            System.out.println("    Durability: " + weapon.getDurability());
            System.out.println("    Cooldown: " + weapon.getCoolDown());
            System.out.println("-----------------------------------");
        }
        System.out.println("Enchantments:");
        for (Enchantment enchantment : enchantments) {
            System.out.println("  Name: " + enchantment.getName());
            System.out.println("    Count: " + enchantment.getCount());
            System.out.println("    Description: " + enchantment.getDescription());
            System.out.println("    Change: " + enchantment.getChange());
            System.out.println("-----------------------------------");
        }
        System.out.println("Items:");
        for (Item item : items) {
            System.out.println("  Name: " + item.getName());
            System.out.println("    Count: " + item.getCount());
            System.out.println("    Description: " + item.getDescription());
            System.out.println("    Group: " + item.getGroup());
            System.out.println("-----------------------------------");
        }
        System.out.println("Infos:");
        for (Info info : infos) {
            System.out.println("  Name: " + info.getName());
            System.out.println("    Count: " + info.getCount());
            System.out.println("    Description: " + info.getDescription());
            System.out.println("    Group: " + info.getGroup());
            System.out.println("-----------------------------------");
        }
        System.out.println("Locations:");
        for (Location location : locations) {
            System.out.println("  Name: " + location.getName());
            System.out.println("    Description: " + location.getDescription());
            System.out.println("    Possible Events: " + location.getPossibleEvents());
            System.out.println("-----------------------------------");
        }
        System.out.println("Events:");
        for (Event event : events) {
            System.out.println("  Name: " + event.getName());
            System.out.println("    Description: " + event.getDescription());
            System.out.println("    Effect: " + event.getEffect().getName());
            System.out.println("    Effect Count: " + event.getEffect().getCount());
            System.out.println("-----------------------------------");
        }
        System.out.println("Difficulties:");
        for (Player player1 : players) {
            System.out.println("  Name: " + player1.getName());
            System.out.println("  Difficulty: " + player1.getDifficultySlogan());
            System.out.println("  Health: " + player1.health);
            System.out.println("  Max Health: " + player1.getMaxHealth());
            System.out.println("  Respawn: " + player1.isRespawn());
            System.out.println("  Weapon: " + player1.getWeapon());
            System.out.println("  Enchantments: " + player1.getEnchantments());
            System.out.println("  Items: " + player1.getItems());
            System.out.println("  Infos: " + player1.getInfos());
            System.out.println("-----------------------------------");
        }

        if (player != null) {
            System.out.println("Current Player:");
            System.out.println("  Name: " + player.getName());
            System.out.println("  Difficulty: " + player.getDifficultySlogan());
            System.out.println("  Health: " + player.health);
            System.out.println("  Max Health: " + player.getMaxHealth());
            System.out.println("  Primary Weapon: " + player.primaryWeapon);
            System.out.println("  Weapons: " + player.getWeapon());
            System.out.println("  Enchantments: " + player.getEnchantments());
            System.out.println("  Items: " + player.getItems());
            System.out.println("  Infos: " + player.getInfos());
            System.out.println("  Respawn: " + player.isRespawn());
            System.out.println("-----------------------------------");
        }
    }

    /**
     * Prints All Entities in detail
     */
    public void printPlayerInfo() {
        if (player == null) {
            System.out.println("no Player defined");
            return;
        }
        System.out.println("Current Player:");
        System.out.println("  Name: " + player.getName());
        System.out.println("  Difficulty: " + player.getDifficultySlogan());
        System.out.println("  Health: " + player.health);
        System.out.println("  Max Health: " + player.getMaxHealth());
        System.out.println("  Primary Weapon: " + player.primaryWeapon);
        System.out.println("  Weapons: " + player.getWeapon());
        System.out.println("  Enchantments: " + player.getEnchantments());
        System.out.println("  Items: " + player.getItems());
        System.out.println("  Infos: " + player.getInfos());
        System.out.println("  Respawn: " + player.isRespawn());
        System.out.println("-----------------------------------");

    }

    /**
     * Lets you chose Player Difficulty
     */
    public void chosePlayerDifficulty() {
        while (true) {
            StringBuilder message = new StringBuilder("Chose one of the difficulties:" + "\n");
            for (Player player : players) {
                message.append(" - ").append(player.getDifficultySlogan()).append(" ( ").append(player.getDifficulty()).append(" ) ").append(player.getDifficultyCode()).append("\n");
            }
            int difficulty = getInputInt(message.toString());
            for (Player player : this.players) {
                if (player.getDifficultyCode() == difficulty) {
                    this.player = player;
                    return;
                }
            }
            System.out.println("Player could not be set correctly, try again");
        }
    }

    /**
     * Configures the name, by asking the user if not hard or very hard
     */
    public void configurePlayerName() {
        if (!player.getName().isEmpty()) {
            player.configure();
            return;
        }
        player.configure(getInput("How would you like to be known under: "));
    }

    /**
     * Configures the name, by parameter
     * @param name String
     */
    public void configurePlayerName(String name) {
        player.configure(name);
    }

    /**
     * Wander around function, to get a random location displayed and an events following an effect on the player
     */
    public void wanderAround() {
        if (player == null) {
            System.out.println("No player is configured yet.");
            return;
        }

        if (locations.isEmpty()) {
            System.out.println("There are no locations to wander around in.");
            return;
        }

        Location location = locations.get(ThreadLocalRandom.current().nextInt(locations.size()));
        System.out.println("You wander around and arrive at " + location.getName() + ".");
        System.out.println(location.getDescription());

        processEvent(location.getPossibleEvents());
    }

    /**
     * Displays a random event. And property process effect
     * @param possibleEvents List<String>
     */
    private void processEvent(List<String> possibleEvents) {
        if (possibleEvents == null || possibleEvents.isEmpty()) {
            System.out.println("Nothing happens here.");
            return;
        }
        try {
            String eventName = possibleEvents.get(ThreadLocalRandom.current().nextInt(possibleEvents.size() * 2));

            Event event = null;
            for (Event candidate : events) {
                if (candidate.getName().equals(eventName)) {
                    event = candidate;
                    break;
                }
            }

            if (event == null) {
                System.out.println("Something feels off, but nothing notable happens.");
                return;
            }
            System.out.println(event.getDescription());

            processEffect(event.getEffect());
        } catch (Exception _) {
            System.out.println("Something feels off, but nothing notable happens.");
        }
    }

    /**
     * Processes Effect for player
     * @param effect EventEffect
     */
    private void processEffect(EventEffect effect) {
        if (effect == null) {
            return;
        }
        System.out.println("Effect: " + effect.getName() + " (" + effect.getValue() + ")");
        this.player = effect.processes(this.player);
    }

    public boolean playerAlive() {
        player.validateAlive();
        return player.getAlive();
    }
}
