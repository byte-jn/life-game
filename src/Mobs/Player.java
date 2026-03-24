package Mobs;

import Items.Weapon;
import java.util.ArrayList;

public class Player extends Entity {
    private ArrayList<String> weapon;
    private ArrayList<String> enchantments;

    public Player() {
        super();
        this.weapon = new ArrayList<>();
    }

    public Player(String name, int health, ArrayList<String> weapon) {
        super(name, health);
        this.weapon = weapon;
    }

    public ArrayList<String> getWeapon() {
        return weapon;
    }

    public void setWeapon(ArrayList<String> weapon) {
        this.weapon = weapon;
    }

    public ArrayList<String> getEnchantments() {
        return enchantments;
    }

    public void setEnchantments(ArrayList<String> enchantments) {
        this.enchantments = enchantments;
    }
}
