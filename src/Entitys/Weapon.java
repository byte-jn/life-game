package Entitys;

public class Weapon {
    private String name;
    private double durability;
    private double damage;
    private double coolDown;
    private int count = 1;

    public Weapon() {}

    public Weapon(String name, double durability, double damage, double coolDown) {
        this.name = name;
        this.durability = durability;
        this.damage = damage;
        this.coolDown = coolDown;
    }

    public Weapon(String name, double durability, double damage, double coolDown, int count) {
        this(name, durability, damage, coolDown);
        this.count = Math.max(1, count);
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

    public int getCount() {
        return count;
    }

    public void setCount(int count) {
        this.count = Math.max(1, count);
    }

    public void increaseCount() {
        increaseCount(1);
    }

    public void increaseCount(int amount) {
        this.count = Math.max(1, this.count + Math.max(0, amount));
    }

    @Override
    public String toString() {
        return name + " x" + count;
    }
}
