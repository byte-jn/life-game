package Entitys;

import java.util.ArrayList;

public class MobEntity extends Entity {
    private ArrayList<String> weapon;

    public MobEntity() {
        super();
    }

    public MobEntity(String name, int health, ArrayList<String> weapon) {
        super(name, health);
        this.weapon = weapon;
    }

    public ArrayList<String> getWeapon() {
        return weapon;
    }
}
