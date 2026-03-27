package Entitys;

public class Weapon {
    private String name;
    private double durability;
    private double damage;
    private double coolDown;

    public Weapon() {}

    public Weapon(String name, double durability, double damage, double coolDown) {
        this.name = name;
        this.durability = durability;
        this.damage = damage;
        this.coolDown = coolDown;
    }

    public String getName() {
        return name;
    }

    public double getDurability() {
        return durability;
    }

    public double getDamage() {
        return damage;
    }

    public double getCoolDown() {
        return coolDown;
    }
}
