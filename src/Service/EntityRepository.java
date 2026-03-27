package Service;

import Entitys.Weapon;
import Entitys.Enchantment;
import Entitys.MobEntity;
import Entitys.Location;
import Entitys.Event;
import Entitys.Player;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.File;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class EntityRepository {
    public static List<MobEntity> getMobEntities() throws Exception {
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

    public static List<Weapon> getWeapons() throws Exception {
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

    public static List<Enchantment> getEnchantments() throws Exception {
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

    public static List<Location> getLocations() throws Exception {
        ObjectMapper mapper = new ObjectMapper();
        File folder = new File("resources/data/locations");

        if (!folder.exists()) {
            throw new Exception("No Folder can be found");
        }

        List<Location> locations = new ArrayList<>();

        for (File file : Objects.requireNonNull(folder.listFiles())) {
            if (file.getName().endsWith(".json")) {
                Location location = mapper.readValue(file, Location.class);
                locations.add(location);
            }
        }
        return locations;
    }

    public static List<Event> getEvents() throws Exception {
        ObjectMapper mapper = new ObjectMapper();
        File folder = new File("resources/data/events");

        if (!folder.exists()) {
            throw new Exception("No Folder can be found");
        }

        List<Event> events = new ArrayList<>();

        for (File file : Objects.requireNonNull(folder.listFiles())) {
            if (file.getName().endsWith(".json")) {
                Event event = mapper.readValue(file, Event.class);
                events.add(event);
            }
        }
        return events;
    }

    public static List<Player> getPlayers() throws Exception {
        ObjectMapper mapper = new ObjectMapper();
        File folder = new File("resources/data/initialPlayer");

        if (!folder.exists()) {
            throw new Exception("No Folder can be found");
        }

        List<Player> players = new ArrayList<>();

        for (File file : Objects.requireNonNull(folder.listFiles())) {
            if (file.getName().endsWith(".json")) {
                Player player = mapper.readValue(file, Player.class);
                players.add(player);
            }
        }
        return players;
    }
}