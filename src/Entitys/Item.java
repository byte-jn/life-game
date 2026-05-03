package Entitys;

public class Item {
    private String name;
    private String description;
    private String group;

    public Item() {}

    public Item(String name, String description, String group) {
        this.name = name;
        this.description = description;
        this.group = group;
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

    @Override
    public String toString() {
        return name;
    }
}
