package Mobs;

import Items.Weapon;

import java.util.ArrayList;

public class MobEntity {
    private String name;
    private int health;
    private ArrayList<Weapon> weapon;

    public MobEntity() {}

    public MobEntity(String name, int health, ArrayList<Weapon> weapon) {
        this.name = name;
        this.health = health;
        this.weapon = weapon;
    }

    public String getName() {
        return name;
    }

    public int getHealth() {
        return health;
    }

    public ArrayList<Weapon> getWeapon() {
        return weapon;
    }
}
