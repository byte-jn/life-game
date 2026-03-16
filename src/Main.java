import Items.Weapon;
import ItemsValue.Enchantment;
import Mobs.MobEntity;
import com.fasterxml.jackson.databind.ObjectMapper;
import java.io.File;
import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class Main {
    public static void main(String[] args) throws Exception {ObjectMapper mapper = new ObjectMapper();
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

        for (MobEntity mob : mobs) {
            System.out.println("Name: " + mob.getName());
            System.out.println("Health: " + mob.getHealth());
            System.out.println("Weapon:");
            for (Weapon weapon : mob.getWeapon()) {
                System.out.println("  Name: " + weapon.getName());
                System.out.println("  Damage: " + weapon.getDamage());
                System.out.println("  CoolDown: " + weapon.getCoolDown());
                System.out.println("  Durability: " + weapon.getDurability());
                System.out.println("  Enchantments: ");
                for (Enchantment enchantment : weapon.getEnchantments()) {
                    System.out.print("      " + enchantment.getName());
                    System.out.print(" (" + enchantment.getDescription() + ")" + "\n");
                }
            }
        }
    }
}