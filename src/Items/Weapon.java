package Items;

import ItemsValue.Enchantment;

import java.util.ArrayList;

public class Weapon {
    private String name;
    private double durability;
    private double damage;
    private double coolDown;
    private ArrayList<Enchantment> enchantments;

    public Weapon() {}

    public Weapon(String name, double durability, double damage, double coolDown, ArrayList<Enchantment> enchantments) {
        this.name = name;
        this.durability = durability;
        this.damage = damage;
        this.coolDown = coolDown;
        this.enchantments = enchantments;
    }

    public String getName() {
        return name;
    }

    public double getDurability() {
        double durability = this.durability;
        for (Enchantment enchantment : enchantments) {
            durability *= enchantment.getChange().getDurabilityIncrease();
        }
        return durability;
    }

    public double getDamage() {
        double damage = this.damage;
        for (Enchantment enchantment : enchantments) {
            damage *= enchantment.getChange().getDamageIncrease();
        }
        return damage;
    }

    public double getCoolDown() {
        double coolDown = this.coolDown;
        for (Enchantment enchantment : enchantments) {
            coolDown *= enchantment.getChange().getCoolDownIncrease();
        }
        return coolDown;
    }

    public ArrayList<Enchantment> getEnchantments() {
        return enchantments;
    }
}
