package ItemsValue;

public class Enchantment {
    private String name;
    private String description;
    private ItemValues change;

    public Enchantment() {}

    public Enchantment(String name, String description, ItemValues change) {
        this.name = name;
        this.description = description;
        this.change = change;
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
}
