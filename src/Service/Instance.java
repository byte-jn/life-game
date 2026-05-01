package Service;

import Entitys.Weapon;
import Entitys.Enchantment;
import Entitys.MobEntity;
import Entitys.Location;
import Entitys.Event;
import Entitys.Player;

import java.util.List;
import java.util.Scanner;

public class Instance {
    public final List<MobEntity> mobs;
    public final List<Weapon> weapons;
    public final List<Enchantment> enchantments;
    public final List<Location> locations;
    public final List<Event> events;
    public Player player;
    public final Scanner scanner = new Scanner(System.in);

    public Instance() throws Exception {
        mobs = EntityRepository.getMobEntities();
        weapons = EntityRepository.getWeapons();
        enchantments = EntityRepository.getEnchantments();
        locations = EntityRepository.getLocations();
        events = EntityRepository.getEvents();

        player = choseDifficulty(EntityRepository.getPlayers());

        configurePlayer();
    }

    private Player choseDifficulty(List<Player> players) {
        System.out.println("Chose one of the difficulties:");
        for (Player player: players) {
            System.out.println(" - " + player.getDifficultySlogan() + " ( " + player.getDifficulty() + " ) " + player.getDifficultyCode());
        }
        System.out.print("\n");

        while (true) {
            String choose = scanner.next();

            Integer chooseDifficulty = getInt(choose);
            if (chooseDifficulty == null) {
                printDifficultCodeIssue(players);
                continue;
            }

            for (Player player : players) {
                if (chooseDifficulty == player.getDifficultyCode()) {
                    return player;
                }
            }

            printDifficultCodeIssue(players);
        }
    }

    private static void printDifficultCodeIssue(List<Player> players) {
        System.out.print("Enter a valid code (");

        for (Player player: players) {
            System.out.print(" " + player.getDifficultyCode());
        }

        System.out.print(" ):\n");
    }

    /**
     * @param s String
     * @return Integer
     */
    private static Integer getInt(String s) {
        try {
            return Integer.parseInt(s);
        } catch (NumberFormatException e) {
            return null;
        }
    }

    /**
     * Configures the name, by asking the user if not hard or very hard
     */
    private void configurePlayer() {
        if (!player.getName().isEmpty()) {
            player.configure();
            return;
        }
        System.out.println("How would you like to be known under: ");
        String name = scanner.next();
        if (name.isEmpty()) {
            name = "William";
        }
        player.configure(name);
    }

    public void testAndPrintEntities() {
        System.out.println("Entities.Mobs:");
        for (MobEntity mob : mobs) {
            System.out.println("  Name: " + mob.getName());
            System.out.println("    Health: " + mob.health);
            System.out.println("    Max Health: " + mob.getMaxHealth());
            System.out.println("    Regeneration Rate: " + mob.getRegenerationRate());
        }
        System.out.println("Weapons:");
        for (Weapon weapon : weapons) {
            System.out.println("  Name: " + weapon.getName());
        }
        System.out.println("Enchantments:");
        for (Enchantment enchantment : enchantments) {
            System.out.println("  Name: " + enchantment.getName());
        }
        System.out.println("Locations:");
        for (Location location : locations) {
            System.out.println("  Name: " + location.getName());
            System.out.println("    Description: " + location.getDescription());
            System.out.println("    Possible Events: " + location.getPossibleEvents());
        }
        System.out.println("Events:");
        for (Event event : events) {
            System.out.println("  Name: " + event.getName());
            System.out.println("    Description: " + event.getDescription());
            System.out.println("    Effect: " + event.getEffect());
        }
        System.out.println("Player:");
        System.out.println("  Name: " + player.getName());
        System.out.println("  Difficulty: " + player.getDifficultySlogan());
        System.out.println("  Health: " + player.health);
        System.out.println("  Max Health: " + player.getMaxHealth());
        System.out.println("  Respawn: " + player.isRespawn());
    }
}