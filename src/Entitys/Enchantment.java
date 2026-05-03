package Entitys;

public class Enchantment {
    private String name;
    private String description;
    private ItemValues change;
    private int count = 1;

    public Enchantment() {}

    public Enchantment(String name, String description, ItemValues change) {
        this.name = name;
        this.description = description;
        this.change = change;
    }

    public Enchantment(String name, String description, ItemValues change, int count) {
        this(name, description, change);
        this.count = Math.max(1, count);
    }

    public String getName() {
        return name;
    }

    public String getDescription() {
        return description;
    }

    public ItemValues getChange() {
        return change;
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
