import Items.Weapon;
import ItemsValue.Enchantment;
import Mobs.MobEntity;
import Locations.Location;
import Events.Event;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.File;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class Main {
    public static void main(String[] args) throws Exception {
        List<MobEntity> mobs = getMobEntities();
        List<Weapon> weapons = getWeapons();
        List<Enchantment> enchantments = getEnchantments();
        List<Location> locations = getLocations();
        List<Event> events = getEvents();

        System.out.println("Mobs:");
        for (MobEntity mob : mobs) {
            System.out.println("  Name: " + mob.getName());
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
    }

    private static List<MobEntity> getMobEntities() throws Exception {
        ObjectMapper mapper = new ObjectMapper();
        File folder = new File("resources/data/mobs");

        if (!folder.exists()) {
            throw new Exception("No Folder can be found");
        }

        List<MobEntity> mobs = new ArrayList<>();

        for (File file : Objects.requireNonNull(folder.listFiles())) {

            if (file.getName().endsWith(".json")) {
                MobEntity mob = mapper.readValue(file, MobEntity.class);
                mobs.add(mob);
            }
        }
        return mobs;
    }

    private static List<Weapon> getWeapons() throws Exception {
        ObjectMapper mapper = new ObjectMapper();
        File folder = new File("resources/data/weapons");

        if (!folder.exists()) {
            throw new Exception("No Folder can be found");
        }

        List<Weapon> weapons = new ArrayList<>();

        for (File file : Objects.requireNonNull(folder.listFiles())) {

            if (file.getName().endsWith(".json")) {
                Weapon weapon = mapper.readValue(file, Weapon.class);
                weapons.add(weapon);
            }
        }
        return weapons;
    }

    private static List<Enchantment> getEnchantments() throws Exception {
        ObjectMapper mapper = new ObjectMapper();
        File folder = new File("resources/data/enchantments");

        if (!folder.exists()) {
            throw new Exception("No Folder can be found");
        }

        List<Enchantment> enchantments = new ArrayList<>();

        for (File file : Objects.requireNonNull(folder.listFiles())) {

            if (file.getName().endsWith(".json")) {
                Enchantment enchantment = mapper.readValue(file, Enchantment.class);
                enchantments.add(enchantment);
            }
        }
        return enchantments;
    }

    private static List<Location> getLocations() throws Exception {
        ObjectMapper mapper = new ObjectMapper();
        File folder = new File("resources/data/locations");
        List<Location> locations = new ArrayList<>();
        for (File file : Objects.requireNonNull(folder.listFiles())) {
            if (file.getName().endsWith(".json")) {
                Location location = mapper.readValue(file, Location.class);
                locations.add(location);
            }
        }
        return locations;
    }

    private static List<Event> getEvents() throws Exception {
        ObjectMapper mapper = new ObjectMapper();
        File folder = new File("resources/data/events");
        List<Event> events = new ArrayList<>();
        for (File file : Objects.requireNonNull(folder.listFiles())) {
            if (file.getName().endsWith(".json")) {
                Event event = mapper.readValue(file, Event.class);
                events.add(event);
            }
        }
        return events;
    }
}