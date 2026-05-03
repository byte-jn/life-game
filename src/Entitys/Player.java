package Entitys;

import Service.EntityRepository;
import com.fasterxml.jackson.annotation.JsonIgnore;
import com.fasterxml.jackson.annotation.JsonSetter;

import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

public class Player {
    @JsonIgnore
    public ArrayList<Weapon> weapon;
    @JsonIgnore
    public ArrayList<Enchantment> enchantments;
    @JsonIgnore
    public ArrayList<Item> items;
    @JsonIgnore
    public ArrayList<Info> infos;
    public Weapon primaryWeapon;
    public int health;
    private String name;
    private int maxHealth;
    private int regenerationRate;
    private String difficulty;
    private int difficultyCode;
    private String difficultySlogan;
    private double enemyDamageMultiplier;
    private boolean noRespawn;
    private boolean dead;

    public Player() {}

    public Player(
            ArrayList<Weapon> weapon,
            ArrayList<Enchantment> enchantments,
            ArrayList<Item> items,
            ArrayList<Info> infos,
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
        this.dead = false;
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

    public ArrayList<Enchantment> getEnchantments() {
        return enchantments;
    }

    @JsonIgnore
    public void setEnchantments(ArrayList<Enchantment> enchantments) {
        this.enchantments = enchantments;
    }

    public ArrayList<Item> getItems() {
        return items;
    }

    @JsonIgnore
    public void setItems(ArrayList<Item> items) {
        this.items = items;
    }

    public ArrayList<Info> getInfos() {
        return infos;
    }

    @JsonIgnore
    public void setInfos(ArrayList<Info> infos) {
        this.infos = infos;
    }

    public ArrayList<Weapon> getWeapon() {
        return weapon;
    }

    @JsonIgnore
    public void setWeapon(ArrayList<Weapon> weapon) {
        this.weapon = weapon;
    }

    @JsonSetter("weapon")
    public void setWeaponNames(List<?> weaponEntries) {
        this.weapon = resolveWeapons(weaponEntries);
    }

    @JsonSetter("enchantments")
    public void setEnchantmentsNames(List<?> enchantmentEntries) {
        this.enchantments = resolveEnchantments(enchantmentEntries);
    }

    @JsonSetter("items")
    public void setItemsNames(List<?> itemEntries) {
        this.items = resolveItems(itemEntries);
    }

    @JsonSetter("infos")
    public void setInfosNames(List<?> infoEntries) {
        this.infos = resolveInfos(infoEntries);
    }

    public String getName() {
        return name;
    }

    public void validateAlive() {
        if (health > 0) {
            return;
        }
        if (hasRevivalTool()) {
            health = (int) Math.round((double) maxHealth * 1.12);
        }
        if (!noRespawn) {
            health = (int) Math.round((double) maxHealth * 0.12);
        }
        dead = true;
    }

    private boolean hasRevivalTool() {
        Item totem = findItemByGroup(items, "revival_tools");
        if (totem == null) {
            return false;
        }
        return totem.getCount() > 0;
    }

    public boolean getAlive() {
        return !dead;
    }

    private ArrayList<Weapon> resolveWeapons(List<?> weaponEntries) {
        ArrayList<Weapon> resolvedWeapons = new ArrayList<>();
        if (weaponEntries == null) {
            return resolvedWeapons;
        }

        try {
            List<Weapon> availableWeapons = EntityRepository.getWeapons();
            for (Object entry : weaponEntries) {
                if (entry instanceof Weapon weapon) {
                    resolvedWeapons.add(weapon);
                    continue;
                }
                if (entry instanceof String weaponName) {
                    Weapon weapon = findWeaponByName(availableWeapons, weaponName);
                    if (weapon != null) {
                        resolvedWeapons.add(weapon);
                    }
                }
            }
        } catch (Exception ignored) {
            // Keep the player usable even if the repository cannot be loaded.
        }
        return resolvedWeapons;
    }

    private ArrayList<Enchantment> resolveEnchantments(List<?> enchantmentEntries) {
        ArrayList<Enchantment> resolvedEnchantments = new ArrayList<>();
        if (enchantmentEntries == null) {
            return resolvedEnchantments;
        }

        try {
            List<Enchantment> availableEnchantments = EntityRepository.getEnchantments();
            for (Object entry : enchantmentEntries) {
                if (entry instanceof Enchantment enchantment) {
                    resolvedEnchantments.add(enchantment);
                    continue;
                }
                if (entry instanceof String enchantmentName) {
                    Enchantment enchantment = findEnchantmentByName(availableEnchantments, enchantmentName);
                    if (enchantment != null) {
                        resolvedEnchantments.add(enchantment);
                    }
                }
            }
        } catch (Exception ignored) {
            // Keep the player usable even if the repository cannot be loaded.
        }
        return resolvedEnchantments;
    }

    private ArrayList<Item> resolveItems(List<?> itemEntries) {
        ArrayList<Item> resolvedItems = new ArrayList<>();
        if (itemEntries == null) {
            return resolvedItems;
        }

        try {
            List<Item> availableItems = EntityRepository.getItems();
            for (Object entry : itemEntries) {
                if (entry instanceof Item item) {
                    resolvedItems.add(item);
                    continue;
                }
                if (entry instanceof String itemName) {
                    Item item = findItemByName(availableItems, itemName);
                    if (item != null) {
                        resolvedItems.add(item);
                    }
                }
            }
        } catch (Exception ignored) {
            // Keep the player usable even if the repository cannot be loaded.
        }
        return resolvedItems;
    }

    private ArrayList<Info> resolveInfos(List<?> infoEntries) {
        ArrayList<Info> resolvedInfos = new ArrayList<>();
        if (infoEntries == null) {
            return resolvedInfos;
        }

        try {
            List<Info> availableInfos = EntityRepository.getInfos();
            for (Object entry : infoEntries) {
                if (entry instanceof Info info) {
                    resolvedInfos.add(info);
                    continue;
                }
                if (entry instanceof String infoName) {
                    Info info = findInfoByName(availableInfos, infoName);
                    if (info != null) {
                        resolvedInfos.add(info);
                    }
                }
            }
        } catch (Exception ignored) {
            // Keep the player usable even if the repository cannot be loaded.
        }
        return resolvedInfos;
    }

    private Weapon findWeaponByName(List<Weapon> weapons, String weaponName) {
        for (Weapon candidate : weapons) {
            if (Objects.equals(candidate.getName(), weaponName)) {
                return candidate;
            }
        }
        return null;
    }

    private Enchantment findEnchantmentByName(List<Enchantment> enchantments, String enchantmentName) {
        for (Enchantment candidate : enchantments) {
            if (Objects.equals(candidate.getName(), enchantmentName)) {
                return candidate;
            }
        }
        return null;
    }

    private Item findItemByName(List<Item> items, String itemName) {
        for (Item candidate : items) {
            if (Objects.equals(candidate.getName(), itemName)) {
                return candidate;
            }
        }
        return null;
    }

    private Item findItemByGroup(List<Item> items, String itemGroupName) {
        for (Item candidate : items) {
            if (Objects.equals(candidate.getGroup(), itemGroupName) && candidate.getCount() > 0) {
                return candidate;
            }
        }
        return null;
    }

    private Info findInfoByName(List<Info> infos, String infoName) {
        for (Info candidate : infos) {
            if (Objects.equals(candidate.getName(), infoName)) {
                return candidate;
            }
        }
        return null;
    }
}
