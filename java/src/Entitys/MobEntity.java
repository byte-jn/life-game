package Entitys;

import java.util.ArrayList;

public class MobEntity {
    public ArrayList<String> weapon;
    public ArrayList<String> enchantments;
    public int health;
    private String name;
    private int maxHealth;
    private int regenerationRate;

    public MobEntity() {}

    public MobEntity(
            ArrayList<String> weapon,
            ArrayList<String> enchantments,
            int health,
            String name,
            int regenerationRate
    ) {
        this.weapon = weapon;
        this.enchantments = enchantments;
        this.name = name;
        this.regenerationRate = regenerationRate;
        this.health = health;
        this.maxHealth = health;
    }

    public void heal() {
        if (health == maxHealth) {
            return;
        }
        if (health + regenerationRate > maxHealth) {
            health = maxHealth;
        }
        health += regenerationRate;
    }

    public int getMaxHealth() {
        return maxHealth;
    }

    public int getRegenerationRate() {
        return regenerationRate;
    }

    public String getName() {
        return name;
    }
}
