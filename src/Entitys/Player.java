package Entitys;

import java.util.ArrayList;

public class Player {
    public ArrayList<String> weapon;
    public ArrayList<String> enchantments;
    public ArrayList<String> items;
    public ArrayList<String> infos;
    public int health;
    private String name;
    private int maxHealth;
    private int regenerationRate;
    private String difficulty;
    private int difficultyCode;
    private String difficultySlogan;
    private double enemyDamageMultiplier;
    private boolean noRespawn;

    public Player() {}

    public Player(
            ArrayList<String> weapon,
            ArrayList<String> enchantments,
            ArrayList<String> items,
            ArrayList<String> infos,
            int health,
            int regenerationRate,
            String difficulty,
            int difficultyCode,
            String difficultySlogan,
            double enemyDamageMultiplier,
            boolean noRespawn
    ) {
        this.weapon = weapon;
        this.enchantments = enchantments;
        this.items = items;
        this.infos = infos;
        this.enemyDamageMultiplier = enemyDamageMultiplier;
        this.regenerationRate = regenerationRate;
        this.difficulty = difficulty;
        this.difficultyCode = difficultyCode;
        this.difficultySlogan = difficultySlogan;
        this.noRespawn = noRespawn;
        this.health = health;
        this.maxHealth = health;
    }

    public void configure(String name) {
        this.name = name;
        this.maxHealth = this.health;
    }

    public void configure() {
        this.maxHealth = this.health;
    }

    public boolean isNoRespawn() {
        return noRespawn;
    }

    public boolean isRespawn() {
        return !noRespawn;
    }

    public String getDifficultySlogan() {
        return difficultySlogan;
    }

    public String getDifficulty() {
        return difficulty;
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

    public void setRegenerationRate(int regenerationRate) {
        this.regenerationRate = regenerationRate;
    }

    public int getDifficultyCode() {
        return difficultyCode;
    }

    public double getEnemyDamageMultiplier() {
        return enemyDamageMultiplier;
    }

    public void setEnemyDamageMultiplier(double enemyDamageMultiplier) {
        this.enemyDamageMultiplier = enemyDamageMultiplier;
    }

    public ArrayList<String> getEnchantments() {
        return enchantments;
    }

    public void setEnchantments(ArrayList<String> enchantments) {
        this.enchantments = enchantments;
    }

    public ArrayList<String> getItems() {
        return items;
    }

    public void setItems(ArrayList<String> items) {
        this.items = items;
    }

    public ArrayList<String> getInfos() {
        return infos;
    }

    public void setInfos(ArrayList<String> infos) {
        this.infos = infos;
    }

    public ArrayList<String> getWeapon() {
        return weapon;
    }

    public void setWeapon(ArrayList<String> weapon) {
        this.weapon = weapon;
    }

    public String getName() {
        return name;
    }
}
