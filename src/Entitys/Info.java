package Entitys;

public class Info {
    private String name;
    private String description;
    private String group;
    private int count = 1;

    public Info() {}

    public Info(String name, String description, String group) {
        this.name = name;
        this.description = description;
        this.group = group;
    }

    public Info(String name, String description, String group, int count) {
        this(name, description, group);
        this.count = Math.max(1, count);
    }

    public String getName() {
        return name;
    }

    public String getDescription() {
        return description;
    }

    public String getGroup() {
        return group;
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
