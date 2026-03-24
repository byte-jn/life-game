package Mobs;

public abstract class Entity {
    protected String name;
    protected int health;

    public Entity() {}

    public Entity(String name, int health) {
        this.name = name;
        this.health = health;
    }

    public String getName() {
        return name;
    }

    public int getHealth() {
        return health;
    }
}
