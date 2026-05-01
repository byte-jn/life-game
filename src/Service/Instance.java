package Service;

import Entitys.Weapon;
import Entitys.Enchantment;
import Entitys.MobEntity;
import Entitys.Location;
import Entitys.Event;
import Entitys.Player;

import java.util.List;

import static Service.MinorFunction.*;

public class Instance {
    public final List<MobEntity> mobs;
    public final List<Weapon> weapons;
    public final List<Enchantment> enchantments;
    public final List<Location> locations;
    public final List<Event> events;
    public final List<Player> players;
    public Player player;

    public Instance() throws Exception {
        mobs = EntityRepository.getMobEntities();
        weapons = EntityRepository.getWeapons();
        enchantments = EntityRepository.getEnchantments();
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
            System.out.println("-----------------------------------");
        }
        System.out.println("Enchantments:");
        for (Enchantment enchantment : enchantments) {
            System.out.println("  Name: " + enchantment.getName());
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
            System.out.println("    Effect: " + event.getEffect());
            System.out.println("-----------------------------------");
        }
        System.out.println("Difficulties:");
        for (Player player1 : players) {
            System.out.println("  Name: " + player1.getName());
            System.out.println("  Difficulty: " + player1.getDifficultySlogan());
            System.out.println("  Health: " + player1.health);
            System.out.println("  Max Health: " + player1.getMaxHealth());
            System.out.println("  Respawn: " + player1.isRespawn());
            System.out.println("-----------------------------------");
        }

        if (player != null) {
            System.out.println("Current Player:");
            System.out.println("  Name: " + player.getName());
            System.out.println("  Difficulty: " + player.getDifficultySlogan());
            System.out.println("  Health: " + player.health);
            System.out.println("  Max Health: " + player.getMaxHealth());
            System.out.println("  Respawn: " + player.isRespawn());
            System.out.println("-----------------------------------");
        }
    }

    /**
     * Lets you chose Player Difficulty
     * @return Player
     */
    public Player chosePlayerDifficulty() {
        StringBuilder message = new StringBuilder("Chose one of the difficulties:" + "\n");
        for (Player player: players) {
            message.append(" - ").append(player.getDifficultySlogan()).append(" ( ").append(player.getDifficulty()).append(" ) ").append(player.getDifficultyCode()).append("\n");
        }
        Integer difficulty = parseInt(getInput(message.toString()));
        if (difficulty == null) return players.getFirst();
        for (Player player : players) {
            if (player.getDifficultyCode() == difficulty) {
                return player;
            }
        }
        return null;
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

    public void wanderAround() {
        // TODO: implement it
    }
}